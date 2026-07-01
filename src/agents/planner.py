from langchain_core.output_parsers import JsonOutputParser

from src.agents.models import ToolDecision
from src.agents.tool_registry import ToolRegistry

from src.llms.llm_factory import LLMFactory

from src.prompts.agent_prompt import (
    get_planner_prompt,
)

from src.agents.planning_context import (
    PlanningContext,
)


class Planner:
    """
    Uses the LLM to decide which tool
    should handle the user's request.
    """

    @staticmethod
    def plan(
        question: str,
        provider: str | None = None,
    ) -> ToolDecision:

        llm = LLMFactory.get_llm(provider)

        parser = JsonOutputParser(
            pydantic_object=ToolDecision
        )

        prompt = (
            get_planner_prompt()
            .partial(
                format_instructions=
                parser.get_format_instructions()
            )
        )

        chain = (
            prompt
            | llm
            | parser
        )

        context = PlanningContext.build()

        return chain.invoke(
            {
                "tools":
                context["tools"],

                "knowledge_base_loaded":
                context["knowledge_base_loaded"],

                "document_count":
                context["document_count"],

                "question":
                question,
            }
        )

        # return ToolDecision(**result)