import uvicorn
import threading
import os
import random
import requests
from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.middleware.cors import CORSMiddleware
from jose import jwt
from passlib.context import CryptContext
import speech_recognition as sr
from pydub import AudioSegment

# --- Configuration ---
ACCESS_TOKEN_EXPIRE_MINUTES = 60
NTFY_TOPIC = "hemanth-genai-alerts-ultimate"
SECRET_KEY = os.getenv("SECRET_KEY", "a-secure-default-secret-key")

# --- Authentication ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
users_db = {"admin": {"username": "admin", "hashed_password": pwd_context.hash("cosmic123")}}

def authenticate_user(u, p):
    user = users_db.get(u)
    return user if u and p and user and pwd_context.verify(p, user["hashed_password"]) else None

def create_access_token(data, expires_delta):
    to_encode = {**data, "exp": datetime.utcnow() + expires_delta}
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if not username or not users_db.get(username):
            raise credentials_exception
    except Exception:
        raise credentials_exception
    return users_db.get(username)

# --- Mobile Alerts ---
def send_ntfy_notification(title, message, priority="default"):
    try:
        requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=message.encode(), headers={"Title": title, "Priority": priority})
        print(f"Sent alert to '{NTFY_TOPIC}': {title}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# --- FastAPI App ---
app = FastAPI(title="Hemanth Generative AI Backend")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user["username"]}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "bearer"}

@app.get("/overview_data", dependencies=[Depends(get_current_user)])
def get_overview_data():
    now = datetime.now()
    return {
        "metrics": {"critical_alerts": random.randint(1, 5), "automations_run": random.randint(100, 200), "cost_savings_est": random.randint(2, 10), "overall_health": "99.8%"},
        "alert_feed": [{"time": (now - timedelta(minutes=i*5)).strftime("%H:%M"), "source": "FusionDB", "message": f"High CPU on node {i}"} for i in range(3)],
        "map_data": {"lat": [12.97, 34.05, 51.50], "lon": [77.59, -118.24, -0.12]}
    }

@app.post("/intake/audio", dependencies=[Depends(get_current_user)])
def intake_audio(audio_file: UploadFile = File(...)):
    recognizer = sr.Recognizer()
    filename = f"/tmp/{audio_file.filename}"
    try:
        with open(filename, "wb") as buffer:
            buffer.write(audio_file.file.read())

        # Convert to WAV if necessary
        if not filename.lower().endswith('.wav'):
            sound = AudioSegment.from_file(filename)
            wav_filename = filename + ".wav"
            sound.export(wav_filename, format="wav")
            target_file = wav_filename
        else:
            target_file = filename

        with sr.AudioFile(target_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        send_ntfy_notification("Voice Command Received", f"Transcribed: '{text}'", priority="high")
        return {"transcribed_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process audio: {str(e)}")
    finally:
        if os.path.exists(filename): os.remove(filename)
        if 'wav_filename' in locals() and os.path.exists(wav_filename): os.remove(wav_filename)
