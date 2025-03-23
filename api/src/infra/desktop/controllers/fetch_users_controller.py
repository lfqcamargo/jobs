from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
from src.domain.users.application.services.fetch_users_service import FetchUsersService
from src.domain.users.enterprise.entities.user import User


class FetchUserController:
    """
    Controller responsible for handling the fetching of users.

    Attributes:
        __service (FetchUsersService): The service responsible for fetching users.
    """

    def __init__(self, service: FetchUsersService) -> None:
        """
        Initializes the FetchUserController with a specific FetchUsersService.

        Args:
            service (FetchUsersService): The service used to fetch the users.
        """
        self.__service = service

    def handle(self) -> list[User]:
        """
        Handles the process of fetching users using the provided service.

        Returns:
            list[User]: A list of users if found.

        Raises:
            ResourNotFoundError: If no users are found.
            ErrorServer: If an internal server error occurs.
        """
        result = self.__service.execute()

        if isinstance(result, Exception):
            if isinstance(result, ResourNotFoundError):
                raise result

            raise ErrorServer("Erro Interno.")

        return result
