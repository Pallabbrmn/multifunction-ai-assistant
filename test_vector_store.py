from src.rag.document_loader import DocumentLoader
from src.rag.text_splitter import TextSplitter
from src.rag.vector_store import VectorStoreService

documents = DocumentLoader.load_document("sample_hr.pdf")
chunks = TextSplitter.split_documents(documents)

vector_store = VectorStoreService.create_vector_store(chunks)

VectorStoreService.save_vector_store(vector_store)

print("Vector store created and saved successfully!")