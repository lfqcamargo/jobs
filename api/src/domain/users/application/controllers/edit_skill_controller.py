from typing import Optional
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.edit_skill_service import EditSkillService
from src.domain.users.application.dto.edit_skill_dto import EditSkillDTO
from src.domain.users.enterprise.enums.skill_level import SkillLevel
from .interfaces.edit_skill_controller_interface import EditSkillControllerInterface


class EditSkillController(EditSkillControllerInterface):
    """
    Controller responsible for handling skill editing requests.

    This controller coordinates the skill editing process. It communicates with the service layer
    to perform the update logic. It raises relevant exceptions if errors are encountered,
    such as when a skill is not found or when domain-related errors occur.
    """

    def __init__(self, service: EditSkillService) -> None:
        """
        Initializes the EditSkillController with a skill service.

        Args:
            service (EditSkillService): The service handling skill editing logic.
        """
        self.__service = service

    def handle(
        self,
        identifier: int,
        description: Optional[str],
        time_month: Optional[int],
        level: Optional[SkillLevel],
    ) -> None:
        dto = EditSkillDTO(
            identifier=identifier,
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
