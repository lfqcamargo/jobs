from src.core.errors.resource_not_found_error import ResourceNotFoundError
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ...enterprise.entities.skill import Skill


class FetchSkillsService:
    """
    Service responsible for retrieving all skills associated with a user.

    This service fetches skills from the repository, ensuring the data is consistent.
    If no skills are found for the user, an error is raised.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initializes the FetchSkillsService with a skills repository.

        Args:
            skills_repository (SkillsRepositoryInterface): The repository responsible for
            retrieving skill data.

        Returns:
            None
        """
        self.__skills_repository = skills_repository

    def execute(self, user_id: int) -> list[Skill] | ResourceNotFoundError:
        """
        Retrieves the list of skills for a specific user.

        This method fetches the skills associated with the provided user ID and
        returns them. If no skills are found for the user, a `ResourceNotFoundError` is raised.

        Args:
            user_id (int): The identifier of the user for whom skills should be fetched.

        Returns:
            list[Skill]: A list of `Skill` objects associated with the given user.

        Raises:
            ResourceNotFoundError: If no skills are found for the specified user.
        """
        skills = self.__skills_repository.fetch_all_by_user(user_id)

        if not skills:
            return ResourceNotFoundError(
                message="Habilidades não encontradas.", resource="Habilidades"
            )

        return skills
