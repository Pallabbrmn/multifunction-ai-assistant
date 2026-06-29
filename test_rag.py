from src.rag.rag_service import RAGService

question = input("Question: ")

response = RAGService.ask(question)

print("\nAnswer\n")
print(response.answer)

print("\nSources\n")

for source in response.sources:

    print("-" * 60)
    print(source.metadata.get("source"))
    print(source.metadata.get("page"))