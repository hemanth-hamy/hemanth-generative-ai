import streamlit as st

def cosmic_card(title, content):
    st.markdown(f'<div class="cosmic-card"><h3>{title}</h3>{content}</div>', unsafe_allow_html=True)
