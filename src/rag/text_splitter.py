from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TextSplitter:
    """
    Splits LangChain Documents into smaller chunks.
    """

    @staticmethod
    def split_documents(
        documents: list[Document],
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> list[Document]:
        """
        Split documents into smaller chunks.

        Args:
            documents: List of LangChain Document objects.
            chunk_size: Maximum characters per chunk.
            chunk_overlap: Number of overlapping characters.

        Returns:
            List of chunked Document objects.
        """

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        return splitter.split_documents(documents)