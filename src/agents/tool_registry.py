from src.tools.chat_tool import ChatTool
from src.tools.rag_tool import RAGTool


class ToolRegistry:
    """
    Central registry for all AI tools.
    """

    _tools = {
        "chat": ChatTool(),
        "rag": RAGTool(),
    }

    @classmethod
    def get_tool(
        cls,
        tool_name: str,
    ):
        """
        Return a tool instance by name.
        """

        return cls._tools.get(
            tool_name.lower()
        )

    @classmethod
    def list_tools(cls):
        """
        Return all registered tool names.
        """

        return list(cls._tools.keys())

    @classmethod
    def get_tool_descriptions(cls):
        """
        Return tool names and descriptions
        for the Planner prompt.
        """

        description = []

        for tool in cls._tools.values():

            description.append(

                f"""
Tool: {tool.name}

Description:
{tool.description}
"""

            )

        return "\n".join(description)

    @classmethod
    def execute(
        cls,
        tool_name: str,
        question: str,
    ):
        """
        Execute a registered tool.
        """

        tool = cls.get_tool(tool_name)

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return tool.execute(question)