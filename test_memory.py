from src.memory.memory_manager import (
    memory
)

memory.add_user_message(
    "Hello"
)

memory.add_ai_message(
    "Hi!"
)

memory.add_user_message(
    "Tell me about React."
)

print(
    memory.get_messages()
)