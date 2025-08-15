import streamlit as st

metrics = [
    {"title": "Active Users (24h)", "value": "7,352", "note": "+291 today"},
    {"title": "Pro Upgrades (Today)", "value": "391", "note": "New record!"},
    {"title": "NFTs Minted", "value": "102", "note": "All cosmic twins"},
    {"title": "Revenue (Today)", "value": "$210", "note": "Total: $53,400"},
    {"title": "Top City", "value": "Bengaluru", "note": "India"},
    {"title": "Support Requests", "value": "4", "note": "All resolved!"},
]
st.markdown('<div class="cosmic-card" style="max-width:1120px;">', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.32rem;font-weight:800;margin-bottom:1.1rem;">📊 3D Cosmic Dashboard & Analytics</div>', unsafe_allow_html=True)
dashboard_html = '<div style="display:flex;gap:2.2rem;justify-content:center;flex-wrap:wrap;">'
for m in metrics:
    dashboard_html += f'''
    <div style="background:linear-gradient(120deg,#232166,#27e1fa22 100%);border-radius:1.6rem;box-shadow:0 0 14px #27e1fa99;padding:1.3rem 2rem;color:#fff;font-size:1.07rem;text-align:center;margin-bottom:1rem;min-width:250px;">
        <div style="font-weight:700;font-size:1.09rem;background:linear-gradient(90deg,#fff,#27e1fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.2rem;">{m["title"]}</div>
        <div style="font-size:1.83rem;font-weight:900;color:#27e1fa;margin-bottom:.2rem;text-shadow:0 2px 14px #ff27fa77;">{m["value"]}</div>
        <div style="font-size:1rem;color:#ff27fa;font-style:italic;">{m["note"]}</div>
    </div>
    '''
dashboard_html += '</div>'
st.markdown(dashboard_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
