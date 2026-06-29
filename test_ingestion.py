from src.ingestion.ingestion_service import (
    IngestionService
)

documents = IngestionService.ingest(
    "sample2.pdf"
)

print(f"Loaded {len(documents)} documents")

print(documents[0].page_content[:500])