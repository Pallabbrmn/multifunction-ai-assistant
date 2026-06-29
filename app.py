import streamlit as st

from src.ui.chat_page import render_chat_page

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
)

render_chat_page()