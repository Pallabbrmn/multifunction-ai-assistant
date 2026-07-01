from src.agents.base_tool import BaseTool

from src.services.chat_service import ChatService


class ChatTool(BaseTool):
    """
    General purpose LLM chat tool.
    """

    name = "chat"

    description = """
Use this tool for:

- General knowledge
- Coding questions
- Writing
- Brainstorming
- General conversation
- Anything that DOES NOT require uploaded documents.
"""

    def execute(
        self,
        question: str,
    ):

        return ChatService.generate_response(
            question
        )