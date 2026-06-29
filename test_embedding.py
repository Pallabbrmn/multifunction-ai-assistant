from src.rag.embeddings import EmbeddingService
from sklearn.metrics.pairwise import cosine_similarity

embeddings = EmbeddingService.get_embeddings()

apple = embeddings.embed_query("Apple")

orange = embeddings.embed_query("Orange")

car = embeddings.embed_query("Car")

print(
    cosine_similarity(
        [apple],
        [orange]
    )
)

print(
    cosine_similarity(
        [apple],
        [car]
    )
)



# vector = embeddings.embed_query(
#     "What is Artificial Intelligence?"
# )

# print(len(vector))

# print(vector[:10])