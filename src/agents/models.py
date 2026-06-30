from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate


class ToolDecision(BaseModel):

    tool: str

    reason: str

