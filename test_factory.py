from src.llms.llm_factory import LLMFactory

llm = LLMFactory.get_llm()

response = llm.invoke(
    "Who won the FIFA World Cup in 2022?"
)

print(response.content)