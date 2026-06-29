from src.rag.document_loader import DocumentLoader
from src.rag.text_splitter import TextSplitter

documents = DocumentLoader.load_document("sample_hr.pdf")

chunks = TextSplitter.split_documents(documents)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")

print("-" * 50)
print(chunks[0].page_content)
print("-" * 50)
print(chunks[0].metadata)