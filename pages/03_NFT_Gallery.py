import streamlit as st
import json

with open("data/nfts.json", "r") as f:
    nft_data = json.load(f)

st.markdown('<div class="cosmic-card" style="max-width: 1200px;">', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.4rem;font-weight:700;margin-bottom:.7rem;">🌠 3D NFT Gallery</div>', unsafe_allow_html=True)
gallery_html = '<div style="display:flex;gap:2.2rem;justify-content:center;flex-wrap:wrap;">'
for n in nft_data:
    gallery_html += f'''
    <div style="width:270px;height:350px;background:linear-gradient(120deg,#1b1d34 75%,#27e1fa33 100%);border-radius:2rem;box-shadow:0 8px 40px #27e1fa66,0 2px 14px #ff27fa44;overflow:hidden;position:relative;transform-style:preserve-3d;animation:spinCard 7s linear infinite;transition:box-shadow .34s;">
        <img src="{n['img']}" style="width:100%;height:66%;object-fit:cover;border-top-left-radius:2rem;border-top-right-radius:2rem;box-shadow:0 2px 22px #00e9fa77;">
        <div style="padding:1.4rem;color:#fff;font-family:'Segoe UI',sans-serif;">
            <h3 style="margin:0;font-size:1.18rem;font-weight:700;background:linear-gradient(90deg,#fff,#27e1fa 70%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">{n["name"]}</h3>
            <p style="margin:.2rem 0 .1rem 0;"><b>Artist:</b> {n["artist"]}</p>
            <p style="margin:.2rem 0;"><b>Price:</b> <span style="color:#27e1fa;">{n["price"]}</span></p>
            <p style="margin:0;"><b>Status:</b> <span style="color:#ff27fa;">Available</span></p>
        </div>
    </div>
    '''
gallery_html += '</div>'
st.markdown(gallery_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
