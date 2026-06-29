from src.rag.retriever import RetrieverService

documents = RetrieverService.retrieve(
    "What are my Leave policies?"
)

print(f"Retrieved {len(documents)} documents")

for index, document in enumerate(documents, start=1):
    print("-" * 50)
    print(f"Chunk {index}")
    print(document.page_content)