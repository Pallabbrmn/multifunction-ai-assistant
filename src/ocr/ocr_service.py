from src.ocr.ocr_factory import OCRFactory
from pathlib import Path


class OCRService:
    """
    High-level OCR orchestration.
    """

    @staticmethod
    def extract_text(
        image_path: str | Path,
        provider: str = "easyocr",
    ) -> str:
        
        image_path = str(image_path)

        ocr = OCRFactory.get_provider(provider)

        return ocr.extract_text(image_path)