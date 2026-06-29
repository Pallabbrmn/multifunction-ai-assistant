from langchain_core.documents import Document

from src.rag.vector_store import VectorStoreService


class RetrieverService:
    """
    Handles retrieval from the vector store.
    """

    @staticmethod
    def retrieve(
        query: str,
        k: int = 4,
    ) -> list[Document]:

        vector_store = VectorStoreService.load_vector_store()

        retriever = vector_store.as_retriever(
            search_kwargs={
                "k": k
            }
        )

        return retriever.invoke(query)