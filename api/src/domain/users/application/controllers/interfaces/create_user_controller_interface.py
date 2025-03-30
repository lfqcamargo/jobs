from abc import ABC, abstractmethod
from datetime import date


class CreateUserControllerInterface(ABC):
    """
    Interface for the user creation controllers.

    This class defines the contract that any implementation of a user creation controller
    must follow. It provides a method to handle user creation requests.

    Methods:
        handle(name: str, email: str, password: str, birthday_date: date,
        curriculum: bytes) -> None:
            Handles the user creation logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(
        self,
        name: str,
        email: str,
        password: str,
        birthday_date: date,
        curriculum: bytes,
    ) -> None:
        """
        Handles the user creation logic.

        This method takes user details as individual arguments and performs the user creation logic.
        It may raise specific exceptions in case of errors, such as `AlreadyExistsError`
        if the user already exists, or `DomainError` for any unexpected domain-related errors.

        Args:
            name (str): The user's name.
            email (str): The user's email address.
            password (str): The user's password.
            birthday_date (date): The user's birthday date.
            curriculum (bytes): The user's curriculum file in binary format (bytes).

        Raises:
            AlreadyExistsError: If the user already exists in the system.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the user creation is successful.
        """
