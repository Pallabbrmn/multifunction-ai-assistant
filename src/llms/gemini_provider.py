from langchain_google_genai import ChatGoogleGenerativeAI

from src.config.settings import (
    GOOGLE_API_KEY,
    GEMINI_MODEL,
    TEMPERATURE,
)


class GeminiProvider:
    """
    Factory class for creating Gemini LLM instances.
    """

    @staticmethod
    def get_llm():
        return ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=TEMPERATURE,
        )