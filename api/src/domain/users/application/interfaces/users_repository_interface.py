from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.user import User


class UsersRepositoryInterface(ABC):
    """
    Interface for the Users Repository.

    This class defines the contract that any implementation of a Users Repository
    must follow. It provides methods to retrieve user data.
    """

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by its email.

        Returns:
            User | None: The user instance if found, otherwise None.
        """

    @abstractmethod
    def create(self, user: User) -> None:
        """
        Persists a new user in the database.

        This method takes a domain entity representing a user and saves it in the database.
        Implementations should handle the persistence logic, ensuring the user data is stored correctly.

        Args:
            user (User): The domain entity representing the user to be stored.

        Returns:
            None
        """
