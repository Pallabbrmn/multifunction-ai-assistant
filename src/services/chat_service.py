from src.llms.llm_factory import LLMFactory
from src.models.chat_models import ChatResponse
from src.utils.logger import get_logger
from src.rag.rag_service import RAGService

logger = get_logger(__name__)


class ChatService:

    @staticmethod
    def generate_response(
        message: str,
        provider: str | None = None,
    ) -> ChatResponse:

        if not message.strip():

            return ChatResponse(
                success=False,
                message="Message cannot be empty.",
                provider="N/A",
            )

        try:

            rag_response = RAGService.ask(
                question=message,
                provider=provider,
            )

            return ChatResponse(
                success=True,
                message=rag_response.answer,
                provider=provider or "default",
            )

        except Exception as e:

            logger.exception(e)

            return ChatResponse(
                success=False,
                message=str(e),
                provider=provider or "default",
            )