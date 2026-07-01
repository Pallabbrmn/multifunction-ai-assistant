from src.agents.tool_registry import ToolRegistry
from src.rag.vector_store import VectorStoreService

from src.utils.logger import get_logger

logger = get_logger(__name__)


class DecisionValidator:
    """
    Validates the planner's selected tool before execution.
    """

    @staticmethod
    def validate(
        tool_name: str,
    ) -> str:
        """
        Validate whether the selected tool
        can actually be executed.

        Returns
        -------
        str
            Final validated tool name.
        """

        tool_name = tool_name.lower().strip()

        # -------------------------------------------------
        # Unknown Tool
        # -------------------------------------------------

        if ToolRegistry.get_tool(tool_name) is None:

            logger.warning(
                "Planner selected unknown tool '%s'. Falling back to chat.",
                tool_name,
            )

            return "chat"

        # -------------------------------------------------
        # RAG Validation
        # -------------------------------------------------

        if tool_name == "rag":

            if not VectorStoreService.index_exists():
                logger.info(
                    "Knowledge base not found. Falling back to chat."
                )
                return "chat"

        return tool_name