from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """
    Interface for the LLM.

    This class defines the contract that any implementation of a LLM
    must follow.
    """

    @abstractmethod
    def run(self) -> str:
        """wait."""
