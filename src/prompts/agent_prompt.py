from langchain_core.prompts import ChatPromptTemplate


def get_agent_prompt():
    """
    Prompt used by the Agent Executor
    to choose one tool.
    """

    return ChatPromptTemplate.from_template(
        """
You are an AI Agent.

Your ONLY job is to choose ONE tool.

Available Tools:

{tools}

Rules:

- Return ONLY the tool name.
- Do not explain your answer.
- Do not answer the user's question.
- Do not return JSON.

User Request:

{question}
"""
    )


def get_planner_prompt():
    """
    Prompt used by the Planner.
    """

    return ChatPromptTemplate.from_template(
        """
You are an intelligent AI Planner.

Your ONLY job is to decide which tool
should execute the user's request.

--------------------------------
Available Tools
--------------------------------

{tools}

--------------------------------
Knowledge Base
--------------------------------

Loaded:
{knowledge_base_loaded}

Number of Documents:
{document_count}

----------------------------
Rules
----------------------------

1. Choose ONLY ONE tool.

2. Use "chat" when:
- General knowledge
- Coding questions
- Writing
- Brainstorming
- General conversation
- Questions that do NOT require uploaded documents

3. Use "rag" when:
- The user refers to uploaded documents
- The user mentions PDF
- The user mentions image
- The user asks about the uploaded file
- The answer should come from the knowledge base

4. Never answer the question.

5. Return ONLY valid JSON.

{format_instructions}

----------------------------
User Request
----------------------------

{question}
"""
    )