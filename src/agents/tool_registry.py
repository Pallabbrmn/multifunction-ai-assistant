from src.agents.base_tool import BaseTool


class ToolRegistry:
    """
    Stores every tool that the AI Agent can use.
    """

    _tools: dict[str, BaseTool] = {}

    @classmethod
    def register(
        cls,
        tool: BaseTool,
    ) -> None:

        cls._tools[
            tool.name
        ] = tool

    @classmethod
    def get_tool(
        cls,
        name: str,
    ) -> BaseTool:

        if name not in cls._tools:

            raise ValueError(
                f"Tool '{name}' not found."
            )

        return cls._tools[name]

    @classmethod
    def list_tools(
        cls,
    ) -> list[str]:

        return list(
            cls._tools.keys()
        )