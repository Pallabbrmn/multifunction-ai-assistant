from langchain_core.prompts import ChatPromptTemplate


def get_agent_prompt():

    return ChatPromptTemplate.from_template(
        """
You are an AI Agent.

Available tools:

{tools}

Your job is to decide which tool
should answer the user's request.

Return ONLY the tool name.

User Request:

{question}
"""
    )


def get_planner_prompt():

    return ChatPromptTemplate.from_template(
"""
You are an AI Agent Planner.

Available tools

{tools}

Your task is to select the SINGLE best tool.

Return

Tool Name

Reason

User Request

{question}
"""
)