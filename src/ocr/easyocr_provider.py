import easyocr

from src.ocr.base_provider import BaseOCRProvider


class EasyOCRProvider(BaseOCRProvider):
    """
    OCR provider using EasyOCR.
    """

    def __init__(self):
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False,
        )

    def extract_text(self, image_path: str) -> str:

        results = self.reader.readtext(
            image_path,
            detail=0,
        )

        return "\n".join(results)