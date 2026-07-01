from src.llms.llm_factory import LLMFactory
from src.models.chat_models import ChatResponse
from src.utils.logger import get_logger

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

            llm = LLMFactory.get_llm(provider)

            response = llm.invoke(message)

            return ChatResponse(
                success=True,
                message=response.content,
                provider=provider or "default",
            )

        except Exception as e:

            logger.exception(e)

            return ChatResponse(
                success=False,
                message=str(e),
                provider=provider or "default",
            )