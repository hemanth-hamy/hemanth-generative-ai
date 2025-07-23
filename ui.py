import streamlit as st
import requests
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Hemanth Gen-AI",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- API & Authentication ---
API_URL = "http://localhost:8000"

if 'token' not in st.session_state:
    st.session_state.token = None
    st.session_state.username = None

def login(username, password):
    try:
        response = requests.post(f"{API_URL}/token", data={"username": username, "password": password})
        if response.status_code == 200:
            st.session_state.token = response.json().get('access_token')
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Login failed. Please check your username and password.")
    except requests.ConnectionError:
        st.error("Connection Error: The backend service is unavailable.")

def logout():
    st.session_state.token = None
    st.session_state.username = None
    st.rerun()

def get_auth_header():
    return {"Authorization": f"Bearer {st.session_state.token}"} if st.session_state.token else None

# --- UI Pages ---
def draw_login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("🌌 Hemanth Generative AI")
        st.header("Enterprise Operations Platform")
        with st.form("login_form"):
            username = st.text_input("Username", value="admin", key="login_user")
            password = st.text_input("Password", type="password", value="cosmic123", key="login_pass")
            if st.form_submit_button("Log In", use_container_width=True):
                login(username, password)

def draw_overview_page():
    st.subheader("Global Operations Dashboard")
    try:
        data = requests.get(f"{API_URL}/overview_data", headers=get_auth_header()).json()
        cols = st.columns(4)
        cols[0].metric("Critical Alerts", data['metrics']['critical_alerts'], "🚨")
        cols[1].metric("Automations Run", data['metrics']['automations_run'], "⚙️")
        cols[2].metric("Cost Savings (Est.)", f"${data['metrics']['cost_savings_est']}k", "+12%")
        cols[3].metric("Overall Health", data['metrics']['overall_health'], "✅")
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("Live Alert Feed")
            for alert in data['alert_feed']:
                st.warning(f"**{alert['time']} - {alert['source']}**: {alert['message']}")
        with col2:
            st.subheader("Global Activity (Conceptual)")
            map_data = pd.DataFrame(data['map_data'])
            st.map(map_data)
    except:
        st.error("Failed to load dashboard data. Is the backend running?")


def draw_intake_page():
    st.subheader("Universal Data Intake")
    tab1, tab2, tab3 = st.tabs(["💬 Text & Logs", "🎤 Voice Commands (via Audio Upload)", "📎 File Upload"])
    with tab2:
        st.subheader("Upload an Audio File")
        audio_file = st.file_uploader("Select a WAV or other audio file", type=['wav', 'mp3', 'm4a'])
        if audio_file is not None and st.button("Transcribe and Process Command"):
            with st.spinner("Uploading and transcribing..."):
                files = {'audio_file': (audio_file.name, audio_file.getvalue(), audio_file.type)}
                res = requests.post(f"{API_URL}/intake/audio", files=files, headers=get_auth_header())
                if res.status_code == 200:
                    st.success("Transcription Complete:")
                    st.code(res.json().get('transcribed_text'), language='text')
                else:
                    st.error(f"Error: {res.text}")

# --- Main App Router ---
if not st.session_state.token:
    draw_login_page()
else:
    with st.sidebar:
        st.title(f"🌌 Welcome, {st.session_state.username}")
        st.markdown("---")
        page = st.radio("Navigation", ["Overview", "Intake & Diagnose"])
        st.markdown("---")
        st.button("Logout", on_click=logout, use_container_width=True)

    if page == "Overview":
        draw_overview_page()
    elif page == "Intake & Diagnose":
        draw_intake_page()
