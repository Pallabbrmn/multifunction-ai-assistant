from src.rag.retriever import RetrieverService

results = RetrieverService.retrieve(
    "What are React Hooks?"
)

print(len(results))

for result in results:
    print(result.content[:300])