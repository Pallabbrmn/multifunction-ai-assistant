from src.agents.register_tools import register_tools
from src.agents.tool_executor import ToolExecutor


register_tools()

answer = ToolExecutor.execute(
    "rag",
    question="What is total spend on TURFXCIMMUNITY?"
)

print(answer)