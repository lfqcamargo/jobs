from src.core.errors.resource_not_found_error import ResourNotFoundError
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ...enterprise.entities.skill import Skill


class FetchSkillsService:
    """
    Service responsible for fetching all skills.

    This class handles the business logic for retrieving skills from the repository.
    If no skills are found, an error is raised. It ensures that the data is consistent
    and properly fetched from the underlying data source.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> list[Skill] | ResourNotFoundError:
        """
        Initializes the FetchSkillsService with a skill repository.

        This service class requires a repository that implements the SkillsRepositoryInterface
        to fetch the list of skills from the data source.

        Args:
            skills_repository (SkillsRepositoryInterface): The repository responsible for
            fetching skill data.

        Returns:
            None
        """
        self.__skills_repository = skills_repository

    def execute(self) -> None:
        """
        Executes the process of fetching skills from the repository.

        It retrieves the list of all skills and raises an error if no skills are found.

        Args:
            None

        Returns:
            list[Skill]: A list of Skill objects representing all skills in the repository.

        Raises:
            ResourNotFoundError: If no skills are found in the repository.
        """
        skills = self.__skills_repository.fetch_all()
        if len(skills) == 0:
            return ResourNotFoundError(message="Skills not found.", resource="skills")

        return skills
