import streamlit as st

from src.ui.chat_page import render_chat_page
from src.ui.sidebar import render_sidebar
from src.ui.upload import render_upload

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
)
st.title("🤖 Multifunction AI Assistant")

render_sidebar()

render_upload()

render_chat_page()