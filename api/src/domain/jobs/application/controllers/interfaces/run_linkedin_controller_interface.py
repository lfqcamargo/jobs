from abc import ABC, abstractmethod


class RunLinkedinControllerInterface(ABC):
    """
    Interface for the RunLinkedinController.

    Defines the contract for handling the execution of the LinkedIn automation
    process based on a provided user ID.

    Methods:
        handle(user_id: int) -> None:
            Initiates the LinkedIn run process for the specified user.
            Must be implemented by any concrete class.
    """

    @abstractmethod
    def handle(self, user_id: int) -> None:
        """
        Handle the LinkedIn run process for a given user ID.

        Args:
            user_id (int): The unique identifier of the user whose LinkedIn
            process should be executed.

        Raises:
            Exception: If an error occurs during the process.
        """
