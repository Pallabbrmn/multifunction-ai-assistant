from langchain_core.documents import Document

from src.rag.document_loader import DocumentLoader

from src.ingestion.base_loader import BaseLoader


class PDFLoader(BaseLoader):
    """
    Loads searchable PDFs.
    """

    def load(
        self,
        file_path: str,
    ) -> list[Document]:

        return DocumentLoader.load_document(
            file_path
        )