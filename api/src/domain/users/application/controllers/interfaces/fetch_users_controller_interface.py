from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.user import User


class FetchUsersControllerInterface(ABC):
    """
    Interface for the user fetching controllers.

    This class defines the contract that any implementation of a user fetching controller
    must follow. It provides a method to handle user fetching requests.

    Methods:
        handle() -> list[User]:
            Handles the user fetching logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(self) -> list[User]:
        """
        Handles the user fetching logic.

        This method retrieves the list of all users.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if no users are found.

        Returns:
            list[User]: A list of User objects representing all users in the system.

        Raises:
            ResourceNotFoundError: If no users are found in the system.
        """
