from abc import ABC, abstractmethod


class BaseOCRProvider(ABC):
    """
    Base class for OCR providers.
    """

    @abstractmethod
    def extract_text(self, image_path: str) -> str:
        """
        Extract text from an image.
        """
        pass