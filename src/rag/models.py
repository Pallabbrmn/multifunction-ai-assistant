from pydantic import BaseModel, ConfigDict

from langchain_core.documents import Document


class RetrievedChunk(BaseModel):
    """
    Represents one retrieved document and its
    similarity score.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )

    document: Document

    score: float

    @property
    def content(self) -> str:
        return self.document.page_content

    @property
    def metadata(self):
        return self.document.metadata
    
class RAGResponse(BaseModel):
    answer: str
    sources: list[RetrievedChunk]