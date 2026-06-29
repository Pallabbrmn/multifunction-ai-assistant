from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:
    """
    Creates embedding models for the RAG pipeline.
    """

    @staticmethod
    def get_embeddings():

        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )