from langchain_groq import ChatGroq

from src.config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL,
    TEMPERATURE,
)


class GroqProvider:
    """
    Factory class for creating Groq LLM instances.
    """

    @staticmethod
    def get_llm():
        return ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_MODEL,
            temperature=TEMPERATURE,
        )