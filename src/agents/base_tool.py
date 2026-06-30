from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for every tool that an AI agent can use.
    """

    name: str
    description: str

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """
        Execute the tool.
        """
        raise NotImplementedError