from src.agents.tool_registry import ToolRegistry

print(
    ToolRegistry.list_tools()
)

print()

print(
    ToolRegistry.get_tool_descriptions()
)

tool = ToolRegistry.get_tool("chat")

print(tool)

# response = ToolRegistry.execute(
#     "chat",
#     "Who is Lionel Messi?"
# )

# print(response)

response = ToolRegistry.execute(
    "rag",
    "What are React Hooks?"
)

print(response.answer)