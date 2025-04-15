from abc import ABC, abstractmethod
from datetime import date


class EditUserControllerInterface(ABC):
    """
    Interface for the user editing controllers.

    This class defines the contract that any implementation of a user editing controller
    must follow. It provides a method to handle user editing requests.

    Methods:
        handle(identifier: int, name: str | None, email: str | None, password: str | None,
               birthday_date: date | None, curriculum: bytes | None) -> None:
            Handles the user editing logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(
        self,
        identifier: int,
        name: str | None,
        email: str | None,
        password: str | None,
        birthday_date: date | None,
        curriculum: bytes | None,
        country_code: str | None,
        phone_number: str | None,
    ) -> None:
        """
        Handles the user editing logic.

        This method takes the user identifier and optional fields for updating user data.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if the user does not exist, or `AlreadyExistsError` if the email is already in use.

        Args:
            identifier (int): The user's unique identifier.
            name (str | None): The user's new name (optional).
            email (str | None): The user's new email (optional).
            password (str | None): The user's new password (optional).
            birthday_date (date | None): The user's new birthday date (optional).
            curriculum (bytes | None): The user's new curriculum file in binary format (optional).
            country_code(str | Nonw): The country code(optional).
            phone_number(str | Nonw): Phone number(optional).

        Raises:
            ResourceNotFoundError: If the user does not exist in the system.
            AlreadyExistsError: If the new email is already in use by another user.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the user editing is successful.
        """
