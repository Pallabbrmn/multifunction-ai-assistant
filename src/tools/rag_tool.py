from src.agents.base_tool import BaseTool

from src.rag.rag_service import RAGService


class RAGTool(BaseTool):

    name = "rag"

    description = """
Use this tool whenever the question
is about uploaded files,
PDFs,
images,
knowledge base,
or stored documents.
"""

    def execute(
        self,
        question: str,
    ):

        return RAGService.ask(question)