import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.header("Settings")

        provider = st.selectbox(
            "LLM Provider",
            [
                "groq",
                "gemini",
            ],
        )

        st.session_state["provider"] = provider