from abc import ABC, abstractmethod


class DeleteQuestionControllerInterface(ABC):
    """
    Interface for the question deletion controllers.

    This class defines the contract that any implementation of a question deletion controller
    must follow. It provides a method to handle question deletion requests.

    Methods:
        handle(identifier: int) -> None:
            Handles the question deletion logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(self, identifier: int) -> None:
        """
        Handles the question deletion logic.

        This method deletes a question by its identifier.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if the question does not exist, or `DomainError` for any unexpected domain-related errors.

        Args:
            identifier (int): Identifier of the question to be deleted.

        Raises:
            ResourceNotFoundError: If the question does not exist in the system.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the question deletion is successful.
        """
