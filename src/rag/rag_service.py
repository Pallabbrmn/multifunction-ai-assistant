from langchain_core.output_parsers import StrOutputParser

from src.llms.llm_factory import LLMFactory
from src.prompts.rag_prompt import get_rag_prompt

from src.rag.retriever import RetrieverService
from src.rag.context_manager import ContextManager
from src.rag.context_builder import ContextBuilder

from src.rag.models import RAGResponse


class RAGService:

    @staticmethod
    def ask(
        question: str,
        provider: str | None = None,
    ) -> RAGResponse:

        retrieved_chunks = RetrieverService.retrieve(
            question
        )

        print("=" * 80)
        print(f"Retrieved {len(retrieved_chunks)} chunks")

        for chunk in retrieved_chunks:
            print(chunk.score)
            print(chunk.document.page_content[:200])
            print("-" * 50)

        prepared_chunks = ContextManager.prepare(
            retrieved_chunks,
            max_chunks=4,
            max_characters=6000,
        )

        context = ContextBuilder.build(
            prepared_chunks,
            include_scores=False,
        )

        llm = LLMFactory.get_llm(provider)

        chain = (
            get_rag_prompt()
            | llm
            | StrOutputParser()
        )

        answer = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return RAGResponse(
            answer=answer,
            sources=prepared_chunks,
        )