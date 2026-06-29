from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from src.rag.embeddings import EmbeddingService

from pathlib import Path

INDEX_PATH = Path("storage/faiss_index")

class VectorStoreService:
    """
    Handles creation, persistence, and loading of the FAISS vector store.
    """

    @staticmethod
    def create_vector_store(
        documents: list[Document],
    ) -> FAISS:
        """
        Create a FAISS vector store from chunked documents.
        """

        embeddings = EmbeddingService.get_embeddings()

        vector_store = FAISS.from_documents(
            documents=documents,
            embedding=embeddings,
        )

        return vector_store
    
    @staticmethod
    def save_vector_store(
        vector_store: FAISS,
    ) -> None:
        """
        Save the FAISS index locally.
        """

        INDEX_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        vector_store.save_local(
            str(INDEX_PATH)
        )

    @staticmethod
    def load_vector_store() -> FAISS:
        """
        Load an existing FAISS vector store.
        """

        embeddings = EmbeddingService.get_embeddings()

        return FAISS.load_local(
            folder_path=str(INDEX_PATH),
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
    
    @staticmethod
    def index_exists() -> bool:
        """
        Check if a saved FAISS index exists.
        """

        return INDEX_PATH.exists()