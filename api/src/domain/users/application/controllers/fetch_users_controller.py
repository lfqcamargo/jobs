from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.fetch_users_service import FetchUsersService
from src.domain.users.enterprise.entities.user import User
from .interfaces.fetch_users_controller_interface import FetchUsersControllerInterface


class FetchUsersController(FetchUsersControllerInterface):
    """
    Controller responsible for handling user fetching requests.

    This controller coordinates the user fetching process. It communicates with the service layer
    to perform the actual retrieval logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when no users are found.

    Methods:
        handle() -> list[User]:
            Handles the user fetching process by calling the service layer.
            If no users are found, a `ResourceNotFoundError` is raised.

    Raises:
        ResourceNotFoundError: If no users exist in the system.
    """

    def __init__(self, service: FetchUsersService) -> None:
        """
        Initializes the FetchUsersController with a user service.

        Args:
            service (FetchUsersService): The service handling user fetching logic.
        """
        self.__service = service

    def handle(self) -> list[User]:
        result = self.__service.execute()

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result

            raise DomainError("Erro interno no servidor.")

        return result
