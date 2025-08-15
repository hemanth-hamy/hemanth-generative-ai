import streamlit as st

avatar = "https://api.dicebear.com/7.x/bottts/svg?seed=hemanth"
user = {
    "name": "Hemanth",
    "location": "Bengaluru, India",
    "pro": True,
    "joined": "2024-12-30",
    "badges": ["Cosmic Pro", "NFT Creator", "Top Referrer", "Contest Winner"],
    "stats": {
        "NFTs Minted": 48,
        "Twins Created": 191,
        "Total Earnings": "$2,300",
        "Rank": "#1 Cosmic"
    }
}
st.markdown('<div class="cosmic-card" style="max-width:470px;">', unsafe_allow_html=True)
st.markdown(f'<img src="{avatar}" style="width:104px;height:104px;border-radius:50%;object-fit:cover;margin-bottom:0.8rem;border:4px solid #27e1fa;box-shadow:0 0 22px #ff27fa88;">', unsafe_allow_html=True)
st.markdown(f'<span style="font-size:1.35rem;font-weight:800;background:linear-gradient(90deg,#fff,#27e1fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.4rem;display:block;">{user["name"]}</span>', unsafe_allow_html=True)
st.markdown(f'<div style="font-size:1.09rem;color:#ff27fa;margin-bottom:1.2rem;">🌍 {user["location"]} | Joined: {user["joined"]}</div>', unsafe_allow_html=True)
if user["pro"]:
    st.markdown('<div style="color:#27e1fa;font-size:1.1rem;font-weight:700;">🌟 Cosmic Pro User</div>', unsafe_allow_html=True)
st.markdown('<div style="display:flex;gap:1.2rem;justify-content:center;margin:1.5rem 0 1rem 0;flex-wrap:wrap;">' + ''.join(
    f'<div style="background:linear-gradient(90deg,#27e1fa 70%,#ff27fa 100%);color:#fff;border-radius:1.6rem;padding:0.52rem 1.2rem;font-weight:700;box-shadow:0 0 20px #27e1fa44;font-size:1.1rem;margin-bottom:0.5rem;border:2.2px solid #fff4;transition:transform .22s;">{badge}</div>' for badge in user["badges"]
) + '</div>', unsafe_allow_html=True)
st.markdown('<div style="display:flex;gap:1.1rem;justify-content:center;margin-top:1.1rem;flex-wrap:wrap;">' + ''.join(
    f'<div style="background:linear-gradient(120deg,#232166,#27e1fa22 100%);border-radius:1.1rem;box-shadow:0 0 10px #27e1fa99;padding:1rem 1.6rem;color:#fff;font-size:1.05rem;text-align:center;margin-bottom:1rem;"><b>{k}</b><br>{v}</div>' for k,v in user["stats"].items()
) + '</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
