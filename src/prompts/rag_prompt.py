from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt() -> ChatPromptTemplate:
    """
    Return the prompt template used by the RAG pipeline.
    """

    return ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

You must answer ONLY using the supplied context.

If the answer is not contained in the context,
respond that you could not find the information
in the provided documents.

If multiple sources mention the same information,
combine them into one clear answer.

Context:
{context}

Question:
{question}
"""
    )