from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.enterprise.entities.skill import Skill
from src.domain.users.application.services.fetch_skills_service import (
    FetchSkillsService,
)
from .interfaces.fetch_skills_controller_interface import FetchSkillsControllerInterface


class FetchSkillsController(FetchSkillsControllerInterface):
    """
    Controller responsible for handling skill fetching requests.

    Delegates the operation to the FetchSkillsService and returns the result or error.
    """

    def __init__(self, service: FetchSkillsService) -> None:
        """
        Initializes the controller with the fetch skills service.

        Args:
            service (FetchSkillsService): Service layer handling the logic.
        """
        self.__service = service

    def handle(self, user_id: int) -> list[Skill]:
        """
        Executes the fetch operation via the service.

        Args:
            user_id (int): Identifier of the user whose skills are being fetched.

        Returns:
            list[Skill]: If skills are found.
        Raise:
            ResourceNotFoundError: If no skills exist for the user.
        """
        result = self.__service.execute(user_id)

        if isinstance(result, ResourceNotFoundError):
            raise result

        return result
