from src.agents.planner import Planner
from src.agents.tool_executor import ToolExecutor

from src.agents.state import AgentState

from src.utils.logger import logger


class AgentExecutor:
    """
    Coordinates the AI agent workflow.

    Responsibilities:
    - Ask the planner to choose a tool.
    - Execute the selected tool.
    - Store reasoning state.
    """

    @staticmethod
    def run(
        question: str,
        provider: str | None = None,
    ):

        state = AgentState(
            user_input=question,
        )

        logger.info(
            "Planning agent execution..."
        )

        decision = Planner.plan(
            question=question,
            provider=provider,
        )

        state.selected_tool = decision.tool

        state.reasoning_steps.append(
            decision.reason
        )

        logger.info(
            "Selected tool: %s",
            decision.tool,
        )

        observation = ToolExecutor.execute(
            decision.tool,
            question=question,
        )

        state.observation = observation
        state.final_answer = observation

        logger.info(
            "Agent execution completed."
        )

        return state