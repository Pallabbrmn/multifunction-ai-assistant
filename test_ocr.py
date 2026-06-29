from src.ocr.ocr_service import OCRService

text = OCRService.extract_text(
    "image_sample.jpeg"
)

print(text)