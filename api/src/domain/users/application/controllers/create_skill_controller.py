from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.create_skill_service import (
    CreateSkillService,
)
from src.domain.users.application.dto.create_skill_dto import CreateSkillDTO
from .interfaces.create_skill_controller_interface import CreateSkillControllerInterface


class CreateSkillController(CreateSkillControllerInterface):
    """
    Controller responsible for handling skill creation requests.

    This controller coordinates the skill creation process. It communicates with the service layer
    to perform the actual creation logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when a user is not found or when domain-related
    errors occur.

    Methods:
        handle(user_id: str, description: str, time_month: int, level: SkillLevel) -> None:
            Handles the skill creation process by calling the service layer with the
            provided skill data. If any errors occur, they are raised appropriately.

    Raises:
        ResourceNotFoundError: If the user is not found in the system.
        DomainError: For any unexpected domain-related errors.
    """

    def __init__(self, service: CreateSkillService) -> None:
        """
        Initializes the CreateSkillController with a skill service.

        Args:
            service (CreateSkillService): The service handling skill creation logic.
        """
        self.__service = service

    def handle(
        self,
        user_id: str,
        description: str,
        time_month: int,
        level: str,
    ) -> None:
        dto = CreateSkillDTO(
            user_id=user_id,
            description=description,
            time_month=time_month,
            level=level,
        )

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
