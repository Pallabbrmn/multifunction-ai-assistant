from src.agents.tool_registry import ToolRegistry

from src.tools.rag_tool import RAGTool
from src.tools.ocr_tool import OCRTool
from src.tools.calculator_tool import CalculatorTool
from src.tools.summarizer_tool import SummarizerTool


def register_tools():

    ToolRegistry.register(
        RAGTool()
    )

    ToolRegistry.register(
        OCRTool()
    )

    ToolRegistry.register(
        CalculatorTool()
    )

    ToolRegistry.register(
        SummarizerTool()
    )

    # ToolRegistry.register(
    #     ChatTool()
    # )