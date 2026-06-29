from src.ingestion.image_loader import ImageLoader

loader = ImageLoader()

documents = loader.load(
    "sample22.jpeg"
)

print(documents[0].page_content)
print(documents[0].metadata)