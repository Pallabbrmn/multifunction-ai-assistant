from src.agents.tool_registry import ToolRegistry

from src.rag.vector_store import VectorStoreService


class PlanningContext:
    """
    Collects information required
    by the Planner before making
    a tool-selection decision.
    """

    @staticmethod
    def build():

        knowledge_base_loaded = (
            VectorStoreService.index_exists()
        )

        document_count = 0

        if knowledge_base_loaded:

            try:

                vector_store = (
                    VectorStoreService.load_vector_store()
                )

                document_count = (
                    vector_store.index.ntotal
                )

            except Exception:

                knowledge_base_loaded = False

                document_count = 0

        return {

            "tools":
            ToolRegistry.get_tool_descriptions(),

            "knowledge_base_loaded":
            knowledge_base_loaded,

            "document_count":
            document_count,

        }