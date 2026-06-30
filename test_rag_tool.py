from src.tools.rag_tool import RAGTool

tool = RAGTool()

response = tool.run(
    question="What did Jun Honda say on the Literature review"
)

print(response)