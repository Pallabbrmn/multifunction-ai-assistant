from src.rag.retriever import RetrieverService
from src.rag.context_builder import ContextBuilder

chunks = RetrieverService.retrieve(
    "What are React Hooks?"
)

context = ContextBuilder.build(
    chunks,
    include_scores=True,
)

print(context)