from src.agents.planner import Planner

decision = Planner.plan(
    "Who is Lionel Messi?"
)

print(decision)

decision = Planner.plan(
    "Summarize my uploaded PDF."
)

print(decision)