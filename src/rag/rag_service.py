from langchain_core.output_parsers import StrOutputParser

from src.llms.llm_factory import LLMFactory
from src.rag.retriever import RetrieverService

from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

If the answer is not contained in the context,
say:

"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}
"""
)

class RAGService:
    """
    Coordinates retrieval and generation.
    """

    @staticmethod
    def ask(
        question: str,
        provider: str | None = None,
    ) -> str:
        
        documents = RetrieverService.retrieve(question)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        llm = LLMFactory.get_llm(provider)

        chain = (
            RAG_PROMPT | llm | StrOutputParser()
        )

        response = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return response