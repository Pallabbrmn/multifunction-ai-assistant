from src.conversation.conversation_models import (
    ConversationMessage,
)


class ConversationManager:
    """
    Handles conversation history.

    This class is independent of
    Streamlit or any UI framework.
    """

    def __init__(self):

        self._messages = []

    def add_user_message(
        self,
        content: str,
    ):

        self._messages.append(

            ConversationMessage(
                role="user",
                content=content,
            )

        )

    def add_assistant_message(
        self,
        content: str,
    ):

        self._messages.append(

            ConversationMessage(
                role="assistant",
                content=content,
            )

        )

    def get_messages(self):

        return self._messages

    def clear(self):

        self._messages.clear()

    def message_count(self):

        return len(self._messages)