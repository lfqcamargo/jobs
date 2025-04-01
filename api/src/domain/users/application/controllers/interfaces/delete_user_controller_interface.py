from abc import ABC, abstractmethod


class DeleteUserControllerInterface(ABC):
    """
    Interface for the user deletion controllers.

    This class defines the contract that any implementation of a user deletion controller
    must follow. It provides a method to handle user deletion requests.

    Methods:
        handle(identifier: int) -> None:
            Handles the user deletion logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(self, identifier: int) -> None:
        """
        Handles the user deletion logic.

        This method takes the user identifier and performs the deletion process.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if the user does not exist, or `DomainError` for any unexpected domain-related errors.

        Args:
            identifier (int): The user's unique identifier.

        Raises:
            ResourceNotFoundError: If the user does not exist in the system.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the user deletion is successful.
        """
