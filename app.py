import os, re, time, uuid, random
from datetime import datetime
import subprocess

import pandas as pd
import streamlit as st

# ---------- Page Config (New Title & Cosmic Theme) ----------
st.set_page_config(
    page_title="ORACLE FUTURE • Hybrid Quantum AI",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
    theme="dark"
)

# ---------- Fresh Cosmic CSS ----------
st.markdown("""
<style>
body {
  background: radial-gradient(circle at 10% 10%, #10162a, #05070e 60%, #02040a 100%);
  background-attachment: fixed;
  color: #e5e7eb;
  font-family: 'Inter', sans-serif;
}
header, footer {
  background: transparent !important;
  visibility: hidden;
}
:root {
  --card-bg: rgba(255,255,255,0.06);
  --card-brd: rgba(255,255,255,0.12);
  --glow-1: 0 10px 40px rgba(99,102,241,.35);
  --glow-2: 0 6px 24px rgba(236,72,153,.25);
}
.hero {
  margin-top: 0.3rem; margin-bottom: 0.8rem; padding: 1rem 1.5rem; border-radius: 20px;
  background: linear-gradient(90deg,rgba(99,102,241,.20),rgba(236,72,153,.20));
  border:1px solid var(--card-brd);
  box-shadow: var(--glow-1),inset 0 0 40px rgba(255,255,255,.05);
}
.glass {background:var(--card-bg); border:1px solid var(--card-brd); border-radius:20px;
box-shadow:var(--glow-2); padding:1.1rem; backdrop-filter:blur(10px);}
.stButton>button{border-radius:12px!important;border:1px solid rgba(255,255,255,.15)!important;
box-shadow:0 8px 18px rgba(0,0,0,.35),inset 0 0 10px rgba(255,255,255,.05); transition:.2s ease;}
.stButton>button:hover{transform:translateY(-1px); box-shadow:0 14px 28px rgba(0,0,0,.45),
0 0 18px rgba(96,165,250,.15);}
section[data-testid="stSidebar"]{background:rgba(17,24,39,.55);backdrop-filter:blur(8px);}
::-webkit-scrollbar{width:8px;}::-webkit-scrollbar-thumb{background:#27e1fa66;border-radius:8px;}
</style>
""", unsafe_allow_html=True)

# ---------- Particle background ----------
def cosmic_particles(n=25):
    html='<div style="position:fixed;width:100vw;height:100vh;left:0;top:0;z-index:-1;pointer-events:none">'
    for _ in range(n):
        left=random.randint(1,98); size=random.randint(8,22)
        d=round(random.uniform(10,18),2); delay=round(random.uniform(0,10),2)
        html+=f'<div style="position:absolute;background:linear-gradient(120deg,#27e1fa,#ff27fa);width:{size}px;height:{size}px;border-radius:50%;opacity:.6;left:{left}vw;bottom:-6vh;animation:move {d}s linear infinite;animation-delay:-{delay}s"></div>'
    html+="""
<style>@keyframes move{0%{transform:translateY(0)scale(.8)}100%{transform:translateY(-95vh)scale(1.4);}}</style>
"""
    html+="</div>"
    return html
st.markdown(cosmic_particles(), unsafe_allow_html=True)

# ---------- Helpers ----------
def card(title, body, maxw=1100):
    st.markdown(f'<div class="glass" style="max-width:{maxw}px;margin:1rem auto;"><h3 style="color:white">{title}</h3>{body}</div>', unsafe_allow_html=True)

def logln(msg): return f"`{time.strftime('%H:%M:%S')}`: {msg}"

@st.cache_data
def sample_csv():
    now=pd.Timestamp.utcnow().floor("min")
    rows=[]; users=["alice","bob","carol","dave"]; ev=["LOGIN","READ","WRITE","DELETE","EXPORT","ERROR"]; sev=["INFO","WARN","ERROR"]
    for i in range(420):
        ts=now-pd.Timedelta(minutes=4*i)
        rows.append({"timestamp":ts.isoformat(),"user":users[i%4],"event":ev[i%6],"severity":sev[i%3]})
    return pd.DataFrame(rows).to_csv(index=False).encode()

def parse_yt(url):
    if not url: return None
    m=re.search(r"(?:v=)([A-Za-z0-9_-]{11})",url) or re.search(r"youtu\.be/([A-Za-z0-9_-]{11})",url) or re.search(r"/shorts/([A-Za-z0-9_-]{11})",url)
    return m.group(1) if m else None

# ---------- Local Whisper if available ----------
def whisper_transcribe(path):
    try:
        import whisper
    except:
        st.warning("Installing whisper (first time)...")
        subprocess.run(["pip","install","--quiet","openai-whisper"])
        import whisper
    model=whisper.load_model("base")
    result=model.transcribe(path)
    return result.get("text","")

# ---------- PDF RAG (chunked) ----------
@st.cache_resource
def load_pdf_chunks(file):
    import fitz
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    doc=fitz.open(stream=file.read(),filetype="pdf")
    text=""
    for page in doc: text+=page.get_text()
    splitter=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=200)
    chunks=splitter.split_text(text)
    return chunks

def rag_search(q, chunks):
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2")
    emb_query=model.encode(q)
    emb_chunks=model.encode(chunks,show_progress_bar=False)
    sims=util.cos_sim(emb_query,emb_chunks)[0]
    top=sorted(zip(sims,chunks), key=lambda x: x[0], reverse=True)[:3]
    return "\n---\n".join([f"{round(float(s),3)}: {c}" for s,c in top])

# ================= HEADER =================
st.markdown("""
<div class="hero">
<h1 style="margin:0;color:white;">🌌 ORACLE FUTURE</h1>
<p style="color:#c7d2fe">Hybrid Autonomous Quantum AI • Works Offline • Unlocks Unlimited When Keys Added</p>
</div>
""", unsafe_allow_html=True)

# ================ MODULES ==================

def mod_audit():
    st.subheader("📊 Audit Log Analyzer")
    st.download_button("Download Sample CSV",data=sample_csv(),file_name="sample.csv")
    upl=st.file_uploader("Upload Audit CSV/JSONL",type=["csv","jsonl"])
    if not upl: st.info("Upload to view charts"); return
    try:
        df=pd.read_json(upl,lines=True) if upl.name.endswith("jsonl") else pd.read_csv(upl)
    except Exception as e:
        st.error(f"Cannot read: {e}"); return
    st.dataframe(df,use_container_width=True)
    if "event" in df.columns:
        c=df["event"].value_counts().rename_axis("event").reset_index(name="count").set_index("event")
        st.bar_chart(c)
    if "timestamp" in df.columns:
        df["timestamp"]=pd.to_datetime(df["timestamp"],errors="coerce")
        df["h"]=df["timestamp"].dt.floor("h")
        s=df.groupby("h")["event"].count().rename("events")
        st.line_chart(s)

def mod_auto():
    st.subheader("🩺 Auto Healing (Sim)")
    if st.button("Start Healing"):
        with st.status("Healing...",expanded=True) as s:
            for m in ["Scanning...","Patching deprecated cache...","Restarting modules..."]:
                st.write(logln(m)); time.sleep(0.7)
            s.update(label="Healed",state="complete")
        st.success("Done.")

def mod_voice():
    st.subheader("🎤 Voice to Text (Local Whisper)")
    wav=st.file_uploader("Upload .wav",type=["wav"])
    if wav and st.button("Transcribe"):
        text=whisper_transcribe(wav)
        st.text_area("Transcript",text,height=200)

def mod_qr():
    st.subheader("🔬 Quantum Reasoning (Sim)")
    if st.button("Run Quantum Reasoning"):
        with st.status("Thinking...",expanded=True) as s:
            for i in range(0,100,10):
                st.write(logln(f"{i}%")); time.sleep(0.2)
            st.write(f"Result Hash: {uuid.uuid4()}")
            s.update(label="Optimized",state="complete")
        st.success("Risk -98% (sim)")

def mod_ocr():
    st.subheader("📺 YouTube Transcript (No Key)")
    url=st.text_input("YouTube URL")
    if st.button("Fetch Transcript"):
        vid=parse_yt(url)
        if not vid: st.error("Bad URL"); return
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
            text=" ".join([x.get("text","") for x in YouTubeTranscriptApi.get_transcript(vid,languages=["en"])])
            st.text_area("Transcript",text,height=250)
        except Exception as e:
            st.error(f"No transcript: {e}")

def mod_doc():
    st.subheader("📎 Intelligent Doc Fixer (Sim)")
    upl=st.file_uploader("PDF / DOCX / TXT",type=["pdf","docx","txt"])
    if upl and st.button("Fix Document"):
        with st.status("Fixing",expanded=True) as s:
            time.sleep(1.5); st.write("✓ Layout aligned"); s.update(label="Fixed",state="complete")
        st.success("Simulated fix complete")

def mod_search():
    st.subheader("🌐 Universal Search (Local-RAG Edition)")
    q=st.text_input("Ask across files or YT",key="q")
    upl=st.file_uploader("Upload PDF (optional)",type=["pdf"])
    if st.button("Search"):
        if upl:
            chunks=load_pdf_chunks(upl)
            ans=rag_search(q,chunks)
            card("PDF Results", ans)
        # Also attempt YT transcript from query if looks like URL
        if "youtube.com" in q or "youtu.be" in q:
            vid=parse_yt(q)
            if vid:
                try:
                    from youtube_transcript_api import YouTubeTranscriptApi
                    text=" ".join([x.get("text","") for x in YouTubeTranscriptApi.get_transcript(vid,languages=["en"])])
                    card("YouTube Transcript", text[:2000]+"...")
                except Exception: pass
        st.success("Search complete.")

def mod_oracle():
    st.subheader("🔍 Oracle Error Resolver (Offline DB)")
    code=st.text_input("Error Code","FRM-40735")
    if st.button("Diagnose"):
        if re.match(r"FRM-40735",code):
            st.write("Likely WHEN-VALIDATE-ITEM trigger failure.")
            st.code("""BEGIN
EXCEPTION WHEN OTHERS THEN
INSERT INTO ERROR_LOG(...) VALUES(...);
RAISE;
END;""",language="sql")
        else:
            st.info("Unknown locally. 🔒 Unlock online resolver by adding Your OpenAI key in .env (COMING SOON)")

def mod_kg():
    st.subheader("🕸️ Knowledge Graph")
    try:
        from pyvis.network import Network
        net=Network(height="650px",width="100%",bgcolor="#0b0f1a",font_color="white")
        net.add_node(0,"ORACLE FUTURE", color="#ff4b4b",size=30)
        for i,t in enumerate(["Audit","Voice","Quantum","RAG","Oracle Fix","Apex"],1):
            net.add_node(i,t,color="#80c4ff",size=14); net.add_edge(0,i)
        st.components.v1.html(net.generate_html(),height=680)
    except Exception as e:
        st.error("PyVis missing"); st.exception(e)

def mod_core():
    st.subheader("🌌 Quantum Core Sim")
    if st.button("Run"):
        with st.status("Running quantum...",expanded=True) as s:
            for i in range(3): time.sleep(0.8); st.write(logln(f"Phase {i+1}/3"))
            s.update(label="Complete",state="complete")
        st.success("Sim OK")

def mod_cosmic():
    st.subheader("🌠 Cosmic Integration Flow")
    card("Flow","Universe → Quantum Core → Oracle Mesh → Human Interface")

def mod_apex():
    st.subheader("🚀 Deploy Apex Universe (Sim)")
    if st.button("Deploy"):
        with st.status("Connecting...",expanded=True) as s:
            for m in ["Authenticating","Deploying to cloud","Activating heal"]:
                time.sleep(1); st.write(m)
            s.update(label="Complete",state="complete")
        st.balloons()
        st.success("Live (sim)")

# ================ NAVIGATION ================
TOOLS=[
"Audit Log Analyzer","Auto Healing Logs","Voice-to-Text","Quantum Reasoning",
"YouTube OCR","Document Fixer","Universal Search","Knowledge Graph",
"Oracle Error Resolution","Quantum Core","Cosmic Integration","Apex Deploy"
]

def set_tool(name):
    st.session_state.sel=name
    st.experimental_set_query_params(tool=name.replace(" ","_"))

params=st.experimental_get_query_params()
urltool=(params.get("tool",[None])[0] or "").replace("_"," ")
if "sel" not in st.session_state:
    st.session_state.sel = urltool if urltool in TOOLS else "Universal Search"

# Quick buttons
row1_cols = st.columns(len(TOOLS)//2)
for i, t in enumerate(TOOLS[:len(TOOLS)//2]):
    with row1_cols[i]:
        if st.button(t, key=f"top_{t}", use_container_width=True):
            set_tool(t)

row2_cols = st.columns(len(TOOLS) - (len(TOOLS)//2))
for i, t in enumerate(TOOLS[len(TOOLS)//2:]):
    with row2_cols[i]:
        if st.button(t, key=f"top_{t}", use_container_width=True):
            set_tool(t)

# Sidebar
with st.sidebar:
    pick=st.radio("Choose Tool",TOOLS,index=TOOLS.index(st.session_state.sel))
    if pick!=st.session_state.sel: set_tool(pick)

ROUTES={
"Audit Log Analyzer":mod_audit,
"Auto Healing Logs":mod_auto,
"Voice-to-Text":mod_voice,
"Quantum Reasoning":mod_qr,
"YouTube OCR":mod_ocr,
"Document Fixer":mod_doc,
"Universal Search":mod_search,
"Knowledge Graph":mod_kg,
"Oracle Error Resolution":mod_oracle,
"Quantum Core":mod_core,
"Cosmic Integration":mod_cosmic,
"Apex Deploy":mod_apex
}

ROUTES[st.session_state.sel]()
# =================== Footer ===================
st.markdown("<center><small>© 2025 Oracle Future AI • Hybrid • Works Offline & Online</small></center>",unsafe_allow_html=True)
