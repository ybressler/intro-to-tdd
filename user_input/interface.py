"""Interface for user input"""

from abc import ABC, abstractmethod
import builtins


class BaseInput(ABC):

    @classmethod
    @abstractmethod
    def input(cls, prompt: str) -> str:
        """
        Read a string from standard input.
        """
        pass


class PurePythonInput(BaseInput):
    """
    Implements a pure python user interface for getting user input,
    using builtin.input()
    """

    @classmethod
    def input(cls, prompt: str) -> str:
        return builtins.input(prompt)
