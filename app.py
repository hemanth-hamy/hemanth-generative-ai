import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from passlib.context import CryptContext

# --- Page Configuration ---
st.set_page_config(
    page_title="Hemanth Gen-AI",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Authentication ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_password = pwd_context.hash("cosmic123")

def check_password(password):
    return pwd_context.verify(password, hashed_password)

# --- Backend Logic (now just Python functions) ---
def get_overview_data():
    now = datetime.now()
    return {
        "metrics": {
            "critical_alerts": random.randint(1, 5),
            "automations_run": random.randint(100, 200),
            "cost_savings_est": random.randint(2, 10),
            "overall_health": "99.8%"
        },
        "alert_feed": [
            {"time": (now - timedelta(minutes=i*5)).strftime("%H:%M"), "source": "FusionDB", "message": f"High CPU on node {i}"} for i in range(3)
        ],
        "map_data": {"lat": [12.97, 34.05, 51.50], "lon": [77.59, -118.24, -0.12]}
    }

# --- UI Pages ---
def draw_login_page():
    st.title("🌌 Hemanth Generative AI Login")
    password = st.text_input("Password", type="password", value="cosmic123")
    if st.button("Log In"):
        if check_password(password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("The password you entered is incorrect.")

def draw_dashboard():
    st.title("Global Operations Dashboard")
    with st.sidebar:
        st.title("Welcome, admin")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

    data = get_overview_data()
    
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

# --- Main App Router ---
if st.session_state.authenticated:
    draw_dashboard()
else:
    draw_login_page()
