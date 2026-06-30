from pathlib import Path
from langchain_core.documents import Document

from src.ingestion.loader_factory import LoaderFactory


class IngestionService:

    @staticmethod
    def ingest(
        file_path: str | Path,
    ) -> list[Document]:

        file_path = str(file_path)   #for OCR

        loader = LoaderFactory.get_loader(
            file_path
        )

        return loader.load(
            file_path
        )