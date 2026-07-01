from src.conversation.conversation_models import (
    ConversationMessage,
)


class HistoryFormatter:
    """
    Converts conversation history
    into prompt text.
    """

    @staticmethod
    def format(
        messages: list[
            ConversationMessage
        ],
    ) -> str:

        history = []

        for message in messages:

            role = message.role.capitalize()

            history.append(

                f"{role}: {message.content}"

            )

        return "\n".join(history)