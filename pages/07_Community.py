import streamlit as st
import json

with open("data/community.json", "r") as f:
    community = json.load(f)

st.markdown('<div class="cosmic-card" style="max-width:900px;">', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.2rem;font-weight:700;margin-bottom:.8rem;">🌐 Cosmic Community Wall</div>', unsafe_allow_html=True)
wall_html = '<div style="display:flex;gap:2.1rem;justify-content:center;flex-wrap:wrap;">'
for m in community:
    wall_html += f'''
    <div style="background:linear-gradient(120deg,#222166,#27e1fa33 100%);border-radius:2.3rem;box-shadow:0 0 18px #27e1fa99;padding:1.2rem 1.7rem;min-width:210px;max-width:260px;color:#fff;font-size:1.04rem;text-align:left;margin-bottom:1.2rem;border:2px solid #fff4;transition:transform .22s,box-shadow .22s;">
        <img src="{m["avatar"]}" style="width:44px;height:44px;border-radius:50%;margin-right:0.7rem;object-fit:cover;border:2.2px solid #fff9;">
        <span style="font-size:1.1rem;font-weight:600;">{m["name"]}</span><br>
        <span style="color:#27e1fa;">{m["city"]}, {m["country"]}</span><br>
        <span>{m["about"]}</span>
    </div>
    '''
wall_html += '</div>'
st.markdown(wall_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
