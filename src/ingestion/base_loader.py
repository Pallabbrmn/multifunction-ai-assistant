from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseLoader(ABC):
    """
    Base interface for all document loaders.
    """

    @abstractmethod
    def load(self, file_path: str) -> list[Document]:
        """
        Convert a file into LangChain Document objects.
        """
        pass