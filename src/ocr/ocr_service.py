from src.ocr.ocr_factory import OCRFactory


class OCRService:
    """
    High-level OCR orchestration.
    """

    @staticmethod
    def extract_text(
        image_path: str,
        provider: str = "easyocr",
    ) -> str:

        ocr = OCRFactory.get_provider(provider)

        return ocr.extract_text(image_path)