from langchain_core.documents import Document

from src.ingestion.loader_factory import LoaderFactory


class IngestionService:
    """
    Converts uploaded files into
    LangChain Document objects.
    """

    @staticmethod
    def ingest(
        file_path: str,
    ) -> list[Document]:

        loader = LoaderFactory.get_loader(
            file_path
        )

        return loader.load(
            file_path
        )