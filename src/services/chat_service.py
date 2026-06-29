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

            logger.warning("Empty message received")

            return ChatResponse(
                success=False,
                message="Message cannot be empty.",
                provider="N/A",
            )

        try:

            logger.info("Getting LLM instance")

            llm = LLMFactory.get_llm(provider)

            logger.info("Invoking LLM")

            response = llm.invoke(message)

            logger.info("Response generated successfully")

            return ChatResponse(
                success=True,
                message=response.content,
                provider=provider or "default",
            )

        except Exception as e:

            logger.exception("Error while generating response")

            return ChatResponse(
                success=False,
                message="Unable to generate response.",
                provider=provider or "default",
            )