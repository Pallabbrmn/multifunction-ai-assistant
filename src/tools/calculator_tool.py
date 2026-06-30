from src.agents.base_tool import BaseTool


class CalculatorTool(BaseTool):

    name="calculator"

    description="Performs arithmetic."

    def run(self, **kwargs):

        expression = kwargs["expression"]

        return str(
            eval(expression)
        )