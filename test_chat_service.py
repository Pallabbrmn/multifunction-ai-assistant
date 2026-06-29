from src.services.chat_service import ChatService


response = ChatService.generate_response(
    "Explain LangChain in simple words."
)

print(response)