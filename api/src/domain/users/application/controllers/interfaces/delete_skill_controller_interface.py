from abc import ABC, abstractmethod


class DeleteSkillControllerInterface(ABC):
    """
    Interface for the skill deletion controllers.

    This class defines the contract that any implementation of a skill deletion controller
    must follow. It provides a method to handle skill deletion requests.

    Methods:
        handle(identifier: int) -> None:
            Handles the skill deletion logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(self, identifier: int) -> None:
        """
        Handles the skill deletion logic.

        This method deletes a skill by its identifier.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if the skill does not exist, or `DomainError` for any unexpected domain-related errors.

        Args:
            identifier (int): Identifier of the skill to be deleted.

        Raises:
            ResourceNotFoundError: If the skill does not exist in the system.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the skill deletion is successful.
        """
