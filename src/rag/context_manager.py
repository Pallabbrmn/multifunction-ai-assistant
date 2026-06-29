from src.rag.models import RetrievedChunk


class ContextManager:
    """
    Selects and prepares retrieved chunks before they
    are formatted into the LLM prompt.
    """

    # @staticmethod
    # def prepare(
    #     chunks: list[RetrievedChunk],
    #     max_chunks: int = 4,
    # ) -> list[RetrievedChunk]:

    #     chunks = sorted(
    #         chunks,
    #         key=lambda chunk: chunk.score
    #     )

    #     return chunks[:max_chunks]
    

    @staticmethod
    def remove_duplicates(
        chunks: list[RetrievedChunk],
    ) -> list[RetrievedChunk]:

        seen = set()

        unique = []

        for chunk in chunks:

            content = chunk.content.strip()

            if content in seen:
                continue

            seen.add(content)

            unique.append(chunk)

        return unique
    
    @staticmethod
    def prepare(
        chunks: list[RetrievedChunk],
        max_chunks: int = 4,
    ) -> list[RetrievedChunk]:

        chunks = ContextManager.remove_duplicates(
            chunks
        )

        chunks = sorted(
            chunks,
            key=lambda chunk: chunk.score
        )

        return chunks[:max_chunks]
    
    @staticmethod
    def limit_context_size(
        chunks: list[RetrievedChunk],
        max_characters: int,
    ) -> list[RetrievedChunk]:

        total = 0

        selected = []

        for chunk in chunks:

            length = len(chunk.content)

            if total + length > max_characters:
                break

            selected.append(chunk)

            total += length

        return selected
    
    @staticmethod
    def prepare(
        chunks: list[RetrievedChunk],
        max_chunks: int = 4,
        max_characters: int = 6000,
    ) -> list[RetrievedChunk]:

        chunks = ContextManager.remove_duplicates(
            chunks
        )

        chunks = sorted(
            chunks,
            key=lambda chunk: chunk.score
        )

        chunks = chunks[:max_chunks]

        chunks = ContextManager.limit_context_size(
            chunks,
            max_characters,
        )

        return chunks