from src.rag.models import RetrievedChunk


class ContextBuilder:
    """
    Converts retrieved chunks into a formatted context
    for the LLM.
    """

    @staticmethod
    def build(
        chunks: list[RetrievedChunk],
        include_scores: bool = False,
    ) -> str:

        sections = []

        for chunk in chunks:

            metadata = chunk.metadata

            source = metadata.get(
                "source",
                "Unknown Source"
            )

            page = metadata.get(
                "page",
                "Unknown"
            )

            score_text = ""

            if include_scores:
                score_text = f"\nScore: {chunk.score:.4f}"

            section = f"""
Source: {source}
Page: {page}{score_text}

Content:
{chunk.content}
"""

            sections.append(section.strip())

        return ("\n" + "-" * 80 + "\n").join(sections)