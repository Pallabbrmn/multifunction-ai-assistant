from src.config.settings import DEFAULT_PROVIDER

from src.llms.gemini_provider import GeminiProvider
from src.llms.groq_provider import GroqProvider


class LLMFactory:
    """
    Factory class responsible for creating
    LLM instances based on the configured provider.
    """

    @staticmethod
    def get_llm(provider: str | None = None):
        """
        Returns an initialized LLM.

        Parameters
        ----------
        provider : str | None
            Optional provider override.

        Returns
        -------
        ChatModel
            LangChain chat model instance.
        """

        provider = (
            provider or DEFAULT_PROVIDER
        ).lower()

        if provider == "groq":
            return GroqProvider.get_llm()

        if provider == "gemini":
            return GeminiProvider.get_llm()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )