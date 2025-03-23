from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
from src.domain.users.application.services.delete_user_service import DeleteUserService


class DeleteUserController:
    """
    Controller responsible for handling the deletion of users.

    Attributes:
        __service (DeleteUserService): The service responsible for deleting users.
    """

    def __init__(self, service: DeleteUserService) -> None:
        """
        Initializes the DeleteUserController with a specific DeleteUserService.

        Args:
            service (DeleteUserService): The service used to delete users.
        """
        self.__service = service

    def handle(self, identifier: int) -> None:
        """
        Handles the process of deleting a user using the provided service.

        Args:
            identifier (int): The identifier of the user to be deleted.

        Raises:
            ResourNotFoundError: If no user is found with the provided identifier.
            ErrorServer: If an internal server error occurs.
        """

        result = self.__service.execute(identifier)

        if isinstance(result, Exception):
            if isinstance(result, ResourNotFoundError):
                raise result

            if isinstance(result, ErrorServer):
                raise result

            raise ErrorServer("Erro Interno.")

        return None
