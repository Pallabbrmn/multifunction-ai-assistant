from src.agents.base_tool import BaseTool

from src.ocr.ocr_service import OCRService


class OCRTool(BaseTool):

    name="ocr"

    description="Extract text from images."

    def run(self, **kwargs):

        image = kwargs["image_path"]

        return OCRService.extract_text(
            image
        )