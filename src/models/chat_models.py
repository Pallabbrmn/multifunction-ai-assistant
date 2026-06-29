from pydantic import BaseModel


class ChatResponse(BaseModel):
    """
    Standard response returned by ChatService.
    """

    success: bool
    message: str
    provider: str