from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.delete_skill_service import (
    DeleteSkillService,
)
from .interfaces.delete_skill_controller_interface import DeleteSkillControllerInterface


class DeleteSkillController(DeleteSkillControllerInterface):
    """
    Controller responsible for handling skill deletion requests.

    This controller coordinates the skill deletion process. It communicates with the service layer
    to perform the actual deletion logic. It raises relevant exceptions if errors are encountered,
    such as when a skill is not found or when domain-related errors occur.

    Methods:
        handle(identifier: int) -> None:
            Handles the skill deletion process.
    """

    def __init__(self, service: DeleteSkillService) -> None:
        """
        Initializes the DeleteSkillController with a skill service.

        Args:
            service (DeleteSkillService): The service handling skill deletion logic.
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
