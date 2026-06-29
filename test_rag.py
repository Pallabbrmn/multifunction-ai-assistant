from src.rag.rag_service import RAGService

question = input("Ask a question: ")

answer = RAGService.ask(question)

print("\nAnswer:\n")
print(answer)