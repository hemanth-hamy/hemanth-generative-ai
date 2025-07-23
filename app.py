# apexzenith_ui_final_v2.py - Immortal AI Daemon UI with Advanced Features
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime, json, os, random, time
from fpdf import FPDF
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import graphviz

# --- Persistent Save Directory ---
SAVE_DIR = "ApexZenith_Daemon_Output"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# --- Initialize Session State ---
if 'diagnosis_result' not in st.session_state:
    st.session_state.diagnosis_result = None
if 'diagnosis_history' not in st.session_state:
    st.session_state.diagnosis_history = []
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
if 'ai_version' not in st.session_state:
    st.session_state.ai_version = 4.0

# --- UI Setup ---
st.set_page_config(page_title="ApexZenith Auto-Healer", layout="wide")

with st.sidebar:
    st.title("🧠 ApexZenith")
    st.markdown("---")
    choice = option_menu(
        menu_title="Navigation",
        options=["Overview", "Diagnose & Chat", "Analytics", "Security", "Optimize", "Integrations"],
        icons=["speedometer2", "chat-dots", "graph-up-arrow", "shield-lock", "cloud-arrow-up", "braces-asterisk"],
        menu_icon="cast",
        default_index=0
    )

# --- Helper Functions for Dynamic Visuals ---
def generate_lineage_graph(version):
    dot = graphviz.Digraph(comment='AI Lineage')
    dot.attr('node', shape='box', style='rounded', fillcolor='lightblue', fontname='sans-serif')
    dot.attr(rankdir='LR', bgcolor='transparent')
    
    dot.node(f'v{version}', f'ApexZenith v{version} (Active)', style='filled', fillcolor='lightgreen')
    if version > 4.0:
        dot.node(f'v{version-0.5}', f'v{version-0.5}')
        dot.edge(f'v{version-0.5}', f'v{version}')
    if version > 4.5:
        dot.node(f'v{version-1.0}', f'v{version-1.0}')
        dot.edge(f'v{version-1.0}', f'v{version-0.5}')
        
    return dot

# --- Overview Page ---
if choice == "Overview":
    st.title("📈 System Overview")
    
    cols = st.columns(4)
    with cols[0]:
        with st.container(border=True): st.metric("Auto-Fixes Today", 72, "+5%")
    with cols[1]:
        with st.container(border=True): st.metric("Diagnosis Accuracy", "99.92%", "+0.02%")
    with cols[2]:
        with st.container(border=True): st.metric("System Uptime", "99.99%", "Stable")
    with cols[3]:
        with st.container(border=True): st.success("Daemon: Active")
    st.markdown("---")

    tab1, tab2 = st.tabs(["🌌 Eternal Intelligence Visuals", "📋 Recent Activity"])

    with tab1:
        st.markdown("### Live Intelligence Matrix")
        
        status_color_map = {"Healthy": "#0F0", "Warning": "#FFD700", "Critical": "#FF0000"}
        status = st.selectbox("Simulate System Status:", options=status_color_map.keys())
        matrix_color = status_color_map[status]

        components.html(f\"\"\"
        <div style='background:black;padding:10px;border-radius:12px;'>
          <canvas id='matrix' width='800' height='300'></canvas>
          <script>
            var c = document.getElementById("matrix");
            var ctx = c.getContext("2d");
            var matrix = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ".split("");
            var font_size = 10;
            var columns = c.width / font_size;
            var drops = [];
            for (var x = 0; x < columns; x++) drops[x] = 1;
            function draw() {{
              ctx.fillStyle = "rgba(0, 0, 0, 0.04)";
              ctx.fillRect(0, 0, c.width, c.height);
              ctx.fillStyle = "{matrix_color}";
              ctx.font = font_size + "px arial";
              for (var i = 0; i < drops.length; i++) {{
                var text = matrix[Math.floor(Math.random() * matrix.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);
                if (drops[i] * font_size > c.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
              }}
            }}
            setInterval(draw, 40);
          </script>
        </div>
        \"\"\", height=320)

        st.markdown("### 🧬 Self-Evolving Agent Lineage")
        st.graphviz_chart(generate_lineage_graph(st.session_state.ai_version))
        if st.button("Simulate AI Evolution"):
            st.session_state.ai_version += 0.5
            st.rerun()

    with tab2:
        st.subheader("Recent Diagnosis History")
        if st.session_state.diagnosis_history:
            history_df = pd.DataFrame(st.session_state.diagnosis_history).tail(5)
            st.dataframe(history_df, use_container_width=True)
        else:
            st.info("No diagnoses have been run in this session yet.")


# --- Diagnose & Chat Page ---
elif choice == "Diagnose & Chat":
    st.title("💬 Chat with ApexZenith Daemon")

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter an error, log, or question..."):
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            ai_response = f"**Diagnosis for `{prompt}`:** This is a simulated AI response. The core issue appears to be related to database connectivity. **Recommendation:** Verify firewall rules and check listener status."
            for chunk in ai_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        st.session_state.chat_messages.append({"role": "assistant", "content": full_response})
        st.session_state.diagnosis_history.append({
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Input": prompt,
            "Diagnosis": ai_response
        })

# --- Other Pages ---
elif choice == "Analytics":
    st.title("📊 Live Analytics Dashboard")
    df = pd.DataFrame({
        "Day": pd.date_range(end=datetime.datetime.today(), periods=7),
        "Automated Fixes": [22, 30, 18, 45, 60, 48, 72],
        "Manual Interventions": [5, 2, 6, 3, 1, 2, 0]
    })
    fig = px.line(df, x="Day", y=["Automated Fixes", "Manual Interventions"], title="System Actions Over Last 7 Days", markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif choice == "Security":
    st.title("🔒 Security & Compliance Events")
    st.warning("🚨 2 login anomalies detected from unusual IPs (auto-blocked)")
    st.success("✅ All compliance checkpoints cleared (CIS Benchmark v8)")

elif choice == "Optimize":
    st.title("☁️ Cloud & Performance Optimization")
    st.success("✅ **Oracle Fusion Instance**: Terminate idle `dev-instance-01` suggested. Estimated savings: $78/month.")
    st.info("ℹ️ **WebLogic Server**: Recommend increasing heap size on `managed-server-3` to resolve performance degradation.")

elif choice == "Integrations":
    st.title("🔌 System Integrations")
    tab1, tab2 = st.tabs(["🎥 YouTube Analyzer", "📢 JIRA Ticketing"])
    with tab1:
        st.subheader("Oracle YouTube Analyzer")
        yt_url = st.text_input("Paste Oracle-related YouTube URL")
        if yt_url and st.button("Analyze & Summarize Video"):
            st.video(yt_url)
            summary = "This video explains the core concepts of Oracle's Subledger Accounting (SLA) framework..."
            st.success(f"**Summary:** {summary}")
            if st.button("Extract Action Items"):
                 st.markdown("- **Action 1:** Review current SLA rules.")
    with tab2:
        st.subheader("Automated JIRA Ticketing")
        issue_summary = st.text_input("Ticket Summary", "FusionDB instance `prod-db-2` showing high latency.")
        if st.button("Create JIRA Ticket"):
            with st.spinner("Submitting ticket..."):
                time.sleep(1)
                ticket_id = f"PROJ-{random.randint(1000, 9999)}"
                st.success(f"✅ Ticket [{ticket_id}](http://your-jira-instance.com/browse/{ticket_id}) successfully created!")

# --- Footer ---
st.markdown("---")
st.markdown("<center><b>ApexZenith v∞</b> | Immortal AI Daemon | Quantum Ready | Live Evolution Graph</center>", unsafe_allow_html=True)
