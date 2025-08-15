import streamlit as st
import json

with open("data/leaderboard.json", "r") as f:
    leaders = json.load(f)

st.markdown('<div class="cosmic-card" style="max-width:560px;">', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.23rem;font-weight:700;margin-bottom:.5rem;">🏆 Cosmic Leaderboard</div>', unsafe_allow_html=True)
for l in leaders:
    st.markdown(f'''
        <div style="margin:0.8rem 0;">
            <img src="{l["avatar"]}" style="width:44px;height:44px;border-radius:50%;margin-right:0.6rem;object-fit:cover;border:2.2px solid #fff9;box-shadow:0 0 18px #27e1fa44;">
            <span style="font-weight:600;font-size:1.13rem;background:linear-gradient(90deg,#fff,#00e9fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">#{l["rank"]} {l["name"]}</span>
            <span style="color:#00e9fa;font-size:1.21rem;margin-left:0.4rem;">{l["score"]}</span>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('<div style="margin-top:1.3rem;color:#fff9;">Anyone can join the leaderboard, earn NFTs, and become a cosmic legend!</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
