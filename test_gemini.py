from src.llms.gemini_provider import GeminiProvider

llm = GeminiProvider.get_llm()

response = llm.invoke(
    "Explain LangChain in one sentence."
)

print(response.content)