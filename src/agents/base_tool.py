from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for every tool
    available to the AI Agent.
    """

    name: str = ""

    description: str = ""

    @abstractmethod
    def execute(
        self,
        question: str,
    ):
        """
        Execute the tool.
        """
        pass