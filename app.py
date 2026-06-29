import streamlit as st

from src.config.settings import GROQ_API_KEY

st.set_page_config(
    page_title="AI Multi-Function App",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Function App")

if GROQ_API_KEY:
    st.success("Groq API Key Loaded Successfully")
else:
    st.warning("Groq API Key Not Found")