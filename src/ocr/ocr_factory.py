from src.ocr.easyocr_provider import EasyOCRProvider


class OCRFactory:

    @staticmethod
    def get_provider(
        provider: str = "easyocr",
    ):

        if provider == "easyocr":
            return EasyOCRProvider()

        raise ValueError(
            f"Unsupported OCR provider: {provider}"
        )