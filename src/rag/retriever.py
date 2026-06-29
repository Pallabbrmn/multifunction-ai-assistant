from src.rag.models import RetrievedChunk
from src.rag.vector_store import VectorStoreService
from src.utils.logger import logger


class RetrieverService:

    @staticmethod
    def retrieve(
        query: str,
        k: int = 4,
        min_score: float | None = None,
    ) -> list[RetrievedChunk]:

        vector_store = VectorStoreService.load_vector_store()

        results = vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )

        logger.info(
            "Searching for: %s",
            query
        )

        retrieved = []

        for document, score in results:

            if (
                min_score is not None
                and score > min_score
            ):
                continue

            retrieved.append(

                RetrievedChunk(
                    document=document,
                    score=float(score),
                )

            )

        logger.info(
            "Retrieved %d chunks",
            len(retrieved)
        )

        return retrieved