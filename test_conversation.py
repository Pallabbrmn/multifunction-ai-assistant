from src.conversation.conversation_manager import (
    ConversationManager
)

from src.conversation.history_formatter import (
    HistoryFormatter
)

conversation = ConversationManager()

conversation.add_user_message(
    "Who is Messi?"
)

conversation.add_assistant_message(
    "Messi is..."
)

conversation.add_user_message(
    "Where was he born?"
)

print(

    HistoryFormatter.format(

        conversation.get_messages()

    )

)