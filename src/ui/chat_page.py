import streamlit as st

from src.services.chat_service import ChatService

from src.conversation.conversation_manager import (
    ConversationManager,
)


def render_chat_page():

    st.title("💬 AI Chat")

    # -----------------------------------
    # Create conversation (once)
    # -----------------------------------

    if "conversation" not in st.session_state:

        st.session_state.conversation = (
            ConversationManager()
        )

    conversation = (
        st.session_state.conversation
    )

    # -----------------------------------
    # Display conversation history
    # -----------------------------------

    for message in conversation.get_messages():

        with st.chat_message(message.role):

            st.markdown(message.content)

    # -----------------------------------
    # Chat Input
    # -----------------------------------

    prompt = st.chat_input(
        "Ask me anything..."
    )

    if prompt:

        # Store user message
        conversation.add_user_message(
            prompt
        )

        # Generate AI response
        with st.spinner("Thinking..."):

            response = ChatService.generate_response(
                prompt
            )

        if response.success:

            # Store assistant reply
            conversation.add_assistant_message(
                response.message
            )

            # Refresh page immediately
            st.rerun()

        else:

            st.error(
                response.message
            )