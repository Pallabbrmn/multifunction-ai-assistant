from src.agents.register_tools import register_tools
from src.agents.agent_executor import AgentExecutor

register_tools()

answer = AgentExecutor.run(
    "What are the total spending on TURFXCOMMUNITY?"
)

print(answer)