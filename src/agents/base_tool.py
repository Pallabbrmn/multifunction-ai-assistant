from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base interface for every agent tool.
    """

    name: str
    description: str

    @abstractmethod
    def run(
        self,
        **kwargs: Any,
    ) -> Any:
        """
        Execute the tool.
        """
        pass