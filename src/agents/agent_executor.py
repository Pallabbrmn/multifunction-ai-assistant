from src.agents.planner import Planner
from src.agents.tool_registry import ToolRegistry

from src.agents.decision_validator import DecisionValidator


class AgentExecutor:

    @staticmethod
    def run(
        question: str,
        provider: str | None = None,
    ):

        decision = Planner.plan(
            question=question,
            provider=provider,
        )

        tool_name = DecisionValidator.validate(
            decision["tool"]
        )

        return ToolRegistry.execute(
            tool_name=tool_name,
            question=question,
        )