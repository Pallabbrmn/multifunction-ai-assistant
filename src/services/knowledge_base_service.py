from pathlib import Path

from src.rag.document_loader import DocumentLoader

from src.ingestion.ingestion_service import (
    IngestionService
)

from src.rag.text_splitter import TextSplitter
from src.rag.embeddings import EmbeddingService
from src.rag.vector_store import VectorStoreService

from src.utils.logger import logger


class KnowledgeBaseService:
    """
    Builds and manages the searchable knowledge base
    from uploaded PDF documents.
    """

    @staticmethod
    def build(
        pdf_path: str,
        force_rebuild: bool = False,
    ):
        """
        Build or load the FAISS knowledge base.

        Args:
            pdf_path: Path to the PDF document.
            force_rebuild: If True, rebuild the index even if one exists.

        Returns:
            FAISS vector store.
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {pdf_path}"
            )

        logger.info("=" * 60)
        logger.info("Knowledge Base Build Started")
        logger.info("=" * 60)

        # -------------------------------------------------
        # Use existing vector store if available
        # -------------------------------------------------

        if (
            not force_rebuild
            and VectorStoreService.index_exists()
        ):
            logger.info(
                "Existing FAISS index found."
            )

            logger.info(
                "Loading cached vector store..."
            )

            vector_store = (
                VectorStoreService.load_vector_store()
            )

            logger.info(
                "Knowledge Base Loaded Successfully."
            )

            return vector_store

        # -------------------------------------------------
        # Load PDF
        # -------------------------------------------------

        logger.info(
            "Loading document..."
        )

        documents = IngestionService.ingest(
            pdf_path
        )

        logger.info(
            "Loaded %d pages.",
            len(documents),
        )

        # -------------------------------------------------
        # Split into chunks
        # -------------------------------------------------

        logger.info(
            "Splitting documents..."
        )

        chunks = TextSplitter.split_documents(
            documents
        )

        logger.info(
            "Created %d chunks.",
            len(chunks),
        )

        # -------------------------------------------------
        # Load embeddings
        # -------------------------------------------------

        logger.info(
            "Loading embedding model..."
        )

        embeddings = (
            EmbeddingService.get_embeddings()
        )

        # -------------------------------------------------
        # Build vector store
        # -------------------------------------------------

        logger.info(
            "Creating FAISS vector store..."
        )

        vector_store = (
            VectorStoreService.create_vector_store(
                documents=chunks,
                embeddings=embeddings,
            )
        )

        # -------------------------------------------------
        # Save vector store
        # -------------------------------------------------

        logger.info(
            "Saving FAISS vector store..."
        )

        VectorStoreService.save_vector_store(
            vector_store
        )

        logger.info(
            "Knowledge Base Built Successfully."
        )

        logger.info("=" * 60)

        return vector_store