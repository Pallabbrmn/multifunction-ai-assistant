from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from src.rag.embeddings import EmbeddingService

from src.utils.logger import logger

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

        if not documents:
            raise ValueError(
                "No documents provided to create the vector store."
            )
        
        logger.info(
            "Loading embedding model..."
        )

        embeddings = EmbeddingService.get_embeddings()

        logger.info(
            "Creating FAISS index..."
        )

        vector_store = FAISS.from_documents(
            documents=documents,
            embedding=embeddings,
        )

        logger.info(
            "FAISS index created."
        )

        return vector_store
    
    @staticmethod
    def save_vector_store(
        vector_store: FAISS,
    ) -> None:
        """
        Save the FAISS index locally.
        """

        # logger.info("Saving FAISS index...")

        INDEX_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        vector_store.save_local(
            str(INDEX_PATH)
        )

        logger.info(
            "Vector store saved."
        )

    @staticmethod
    def load_vector_store() -> FAISS:
        """
        Load an existing FAISS vector store.
        """

        if not VectorStoreService.index_exists():
            raise FileNotFoundError(
                "Knowledge base not found."
            )

        embeddings = EmbeddingService.get_embeddings()

        return FAISS.load_local(
            folder_path=str(INDEX_PATH),
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
    
    @staticmethod
    def index_exists() -> bool:

        return (

            (INDEX_PATH / "index.faiss").exists()

            and

            (INDEX_PATH / "index.pkl").exists()

        )