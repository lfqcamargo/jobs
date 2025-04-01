from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.delete_user_service import DeleteUserService
from .interfaces.delete_user_controller_interface import DeleteUserControllerInterface


class DeleteUserController(DeleteUserControllerInterface):
    """
    Controller responsible for handling user deletion requests.

    This controller coordinates the user deletion process. It communicates with the service layer
    to perform the actual deletion logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when a user does not exist or when domain-related
    errors occur.

    Methods:
        handle(identifier: int) -> None:
            Handles the user deletion process by calling the service layer with the
            provided user identifier.
            If any errors occur (e.g., user not found, domain errors), they are raised
            appropriately.

    Raises:
        ResourceNotFoundError: If the user does not exist in the system.
        DomainError: For any unexpected domain-related errors.
    """

    def __init__(self, service: DeleteUserService) -> None:
        """
        Initializes the DeleteUserController with a user service.

        Args:
            service (DeleteUserService): The service handling user deletion logic.
        """
        self.__service = service

    def handle(self, identifier: int) -> None:
        result = self.__service.execute(identifier)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
