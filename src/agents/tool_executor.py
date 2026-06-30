from typing import Any

from src.agents.tool_registry import (
    ToolRegistry,
)

from src.utils.logger import logger


class ToolExecutor:
    """
    Executes tools from the registry.
    """

    @staticmethod
    def execute(
        tool_name: str,
        **kwargs: Any,
    ) -> Any:

        logger.info(
            "Executing tool: %s",
            tool_name,
        )

        tool = ToolRegistry.get_tool(
            tool_name
        )

        result = tool.run(
            **kwargs
        )

        logger.info(
            "Tool execution completed."
        )

        return result