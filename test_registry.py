from src.agents.register_tools import (
    register_tools,
)

from src.agents.tool_registry import (
    ToolRegistry,
)


register_tools()

print(
    ToolRegistry.list_tools()
)

tool = ToolRegistry.get_tool(
    "rag"
)

print(tool)

print(
    tool.run(
        question="What are the spendings on TURFXCOMMUNITY ?"
    )
)