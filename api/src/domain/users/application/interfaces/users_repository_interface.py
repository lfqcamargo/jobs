from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.user import User


class UsersRepositoryInterface(ABC):
    """
    Interface for the Users Repository.

    This class defines the contract that any implementation of a Users Repository
    must follow. It provides methods to retrieve user data.
    """

    @abstractmethod
    def create(self, user: User) -> bool:
        """
        Persists a new user in the database.

        This method takes a domain entity representing a user and saves it in the database.
        Implementations should handle the persistence logic, ensuring the user data is stored
        correctly.

        Args:
            user (User): The domain entity representing the user to be stored.

        Returns:
            bool
        """

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by its email.

        Returns:
            User | None: The user instance if found, otherwise None.
        """

    @abstractmethod
    def find_by_identifier(self, identifier: int) -> User | None:
        """
        Retrieve a user by its identifier.

        Returns:
            User | None: The user instance if found, otherwise None.
        """

    @abstractmethod
    def fetch_all(self) -> list[User] | None:
        """
        Retrieves all users from the database.

        This method queries the database and returns a list of all user entities stored.
        The implementation should handle the retrieval logic, ensuring that the list of users
        is accurate and complete.

        Returns:
            list[User] | None: A list of User objects representing all users in the database
            or None.
        """

    @abstractmethod
    def save(self, user: User) -> bool:
        """
        Persists a new user in the database.

        This method takes a domain entity representing a user and saves it in the database.
        Implementations should handle the persistence logic, ensuring the user data is stored
        correctly.

        Args:
            user (User): The domain entity representing the user to be stored.

        Returns:
            bool
        """

    @abstractmethod
    def delete(self, identifier: int) -> bool:
        """
        Delete a user by its identifier.

        Returns:
            None: Return None.
        """
