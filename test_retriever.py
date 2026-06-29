from src.rag.retriever import RetrieverService

results = RetrieverService.retrieve(
    "What are the Leave policies?"
)

for chunk in results:

    print("=" * 60)

    print("Score:", chunk.score)

    print("Metadata:", chunk.metadata)

    print(chunk.content)