from src.rag.retriever import RetrieverService

results = RetrieverService.retrieve(
    "What is React?"
)

print(len(results))

for result in results:
    print(result.document.page_content[:300])