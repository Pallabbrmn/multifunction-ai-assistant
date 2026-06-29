import streamlit as st

from src.services.chat_service import ChatService


def render_chat_page():

    st.title("💬 AI Chat")

    prompt = st.text_area(
        "Ask anything"
    )

    if st.button("Generate Response"):

        with st.spinner("Thinking..."):

            response = ChatService.generate_response(
                prompt
            )

        if response.success:

            st.success(response.message)

        else:

            st.error(response.message)