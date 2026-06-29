from src.rag.document_loader import DocumentLoader

docs = DocumentLoader.load_document(
    "sample_hr.pdf"
)

print(docs)

# print(len(docs))

# print(docs[0])