from dataclasses import dataclass, field


@dataclass
class AgentState:
    """
    Stores the current reasoning state of the agent.
    """

    user_input: str

    selected_tool: str | None = None

    tool_input: dict = field(
        default_factory=dict
    )

    observation: str | None = None

    final_answer: str | None = None

    reasoning_steps: list[str] = field(
        default_factory=list
    )