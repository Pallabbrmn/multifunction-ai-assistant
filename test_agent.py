from src.agents.agent_executor import AgentExecutor

response = AgentExecutor.run(
    "Summarize my uploaded document."
)

print(response)