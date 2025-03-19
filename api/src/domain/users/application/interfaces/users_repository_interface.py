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
