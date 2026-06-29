from src.llms.groq_provider import GroqProvider

provider = GroqProvider()

llm = provider.get_llm()

response = llm.invoke("Explain React in one sentence.")

print(response.content)