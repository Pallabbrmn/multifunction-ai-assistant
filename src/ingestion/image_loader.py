from pathlib import Path

from langchain_core.documents import Document

from src.ingestion.base_loader import BaseLoader
from src.ocr.ocr_service import OCRService


class ImageLoader(BaseLoader):
    """
    Converts images into LangChain Documents
    using OCR.
    """

    def load(
        self,
        file_path: str,
    ) -> list[Document]:

        text = OCRService.extract_text(
            file_path
        )

        document = Document(
            page_content=text,
            metadata={
                "source": Path(file_path).name,
                "type": "image",
            },
        )

        return [document]