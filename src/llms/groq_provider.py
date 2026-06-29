from langchain_groq import ChatGroq

from src.config.settings import (
    GROQ_API_KEY,
    DEFAULT_MODEL,
    TEMPERATURE,
)


class GroqProvider:
    """
    Creates and manages a Groq LLM instance.
    """

    def __init__(self):
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=DEFAULT_MODEL,
            temperature=TEMPERATURE,
        )

    def get_llm(self):
        """
        Returns the configured ChatGroq instance.
        """
        return self.llm