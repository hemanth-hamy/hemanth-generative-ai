import streamlit as st
import random
from utils import cosmic_card

st.set_page_config(page_title="CosmicMirror.ai — Apex 3D Universe", page_icon="🌌", layout="wide")

# --- 3D Cosmic Background + Card CSS (shared across all tabs) ---
st.markdown("""
<style>
body { background: #090426;}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #0b0435 10%, #27e1fa33 90%);
    min-height: 100vh; overflow: hidden;
}
.cosmic-particles {
    position: fixed; z-index: -1; width: 100vw; height: 100vh; left: 0; top: 0; pointer-events: none;
}
.particle {
  position: absolute; border-radius: 50%; opacity: .6;
  background: linear-gradient(120deg,#27e1fa,#ff27fa);
  pointer-events: none; animation: moveParticle 19s linear infinite;
}
@keyframes moveParticle {
    0% { transform: translateY(0) scale(.8);}
    100% { transform: translateY(-95vh) scale(1.28);}
}
.cosmic-3d-title {
    font-size: 2.5rem; font-weight: bold;
    background: linear-gradient(90deg, #fff, #00e9fa 50%, #ff27fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-shadow: 0 2px 30px #00e9fa88, 0 0 2px #fff;
    letter-spacing: .1em; margin-bottom: 1rem;
}
.cosmic-nav { display: flex; flex-direction: row; gap: 1.2rem; margin-bottom: 1.7rem; justify-content: center; }
.cosmic-nav button {
    border-radius: 1.2rem;
    background: linear-gradient(100deg,#191637,#27e1fa77 100%);
    color: #fff; font-size: 1.05rem; font-weight: 500;
    padding: 0.7rem 2.1rem; border: none;
    box-shadow: 0 0 18px 2px #00e9fa33; margin: 0; cursor: pointer;
    transition: all 0.22s;
}
.cosmic-nav button.selected, .cosmic-nav button:hover {
    background: linear-gradient(100deg, #27e1fa 30%, #ff27fa 100%);
    color: #fff; transform: scale(1.07) rotate(-1deg);
    box-shadow: 0 0 40px 8px #ff27fa77;
}
::-webkit-scrollbar-thumb { background: #27e1fa66; border-radius: 8px;}
::-webkit-scrollbar { width: 10px;}
.cosmic-card {
    border-radius: 2rem;
    box-shadow: 0 0 40px 10px #27e1fa55, 0 0 4px 1px #fff6;
    background: rgba(23,27,44,0.99);
    padding: 2.2rem 2.1rem 2rem 2.1rem;
    margin: 2.1rem auto 1.2rem auto;
    color: #fff;
    max-width: 530px;
    transition: box-shadow 0.4s;
}
.cosmic-card:hover {
    box-shadow: 0 0 60px 16px #ff27facc, 0 0 8px 2px #00e9e966;
}
</style>
""", unsafe_allow_html=True)

# --- Animated Particle Background ---
def particles_html(n=28):
    html = '<div class="cosmic-particles">'
    for _ in range(n):
        left = random.randint(1, 98)
        size = random.randint(9, 26)
        dur = round(random.uniform(10, 22),2)
        delay = round(random.uniform(0,11),2)
        html += f'<div class="particle" style="left:{left}vw; bottom:-7vh;width:{size}px;height:{size}px;animation-duration:{dur}s;animation-delay:-{delay}s;"></div>'
    html += '</div>'
    return html
st.markdown(particles_html(), unsafe_allow_html=True)

# --- Main App ---
st.markdown('<div class="cosmic-3d-title">🌌 CosmicMirror.ai</div>', unsafe_allow_html=True)
st.markdown('<center><i>The Ultimate 3D Cosmic App — All Phases, All Features Unlocked</i></center>', unsafe_allow_html=True)
st.markdown("---")

# --- Home Page Content ---
cosmic_card("Welcome Home, Cosmic Creator 🚀", """
- Convert any file, mint NFTs, chat with digital twins, earn, and lead!
- All features, all languages, all countries, all users: now live.
- Powered by the universe's most advanced cosmic engine.
""")

# --- Footer ---
st.markdown("""
<br>
<center><small>© 2025 CosmicMirror.ai | The Ultimate 3D Cosmic App | All Phases, All Features, All Running 🚀</small></center>
""", unsafe_allow_html=True)
