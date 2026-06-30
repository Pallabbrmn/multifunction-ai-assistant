from typing import Any

from src.agents.base_tool import BaseTool
from src.rag.rag_service import RAGService


class RAGTool(BaseTool):
    """
    Tool for querying the knowledge base.
    """

    name = "rag"

    description = (
        "Searches the uploaded knowledge base "
        "and answers questions using retrieved context."
    )

    def run(self, **kwargs: Any) -> str:

        question = kwargs.get("question")

        if not question:
            raise ValueError(
                "Question is required."
            )

        response = RAGService.ask(question)

        return response.answer