from src.agents.base_tool import BaseTool

from src.llms.llm_factory import LLMFactory


class SummarizerTool(BaseTool):

    name="summarizer"

    description="Summarizes text."

    def run(self, **kwargs):

        llm = LLMFactory.get_llm()

        text = kwargs["text"]

        return llm.invoke(
            "Summarize\n\n"+text
        ).content