from src.agents.agent_executor import AgentExecutor

response = AgentExecutor.run(
    "Summarize my uploaded new updated document."
)

print(response)
