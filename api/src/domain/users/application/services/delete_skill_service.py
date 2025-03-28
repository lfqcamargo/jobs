from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface


class DeleteSkillService:
    """
    Service responsible for deleting a skill.

    This class handles the business logic for deleting a skill by its identifier,
    ensuring that the skill exists before attempting to delete.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initializes the DeleteSkillService with a skill repository.

        Args:
            skills_repository (SkillsRepositoryInterface): The repository responsible for
            skill data operations (find, delete, etc.).
        """
        self.__skills_repository = skills_repository

    def execute(self, identifier: int) -> None:
        """
        Executes the skill deletion process.

        This method checks if the skill with the given identifier exists. If the skill is found,
        it proceeds to delete the skill. If the skill is not found, a `ResourNotFoundError` is raised.

        Args:
            identifier (int): The identifier of the skill to be deleted.

        Raises:
            ResourNotFoundError: If the skill is not found with the given identifier.
            ErrorServer: If an error occurs during the deletion process.

        Returns:
            None
        """
        skill = self.__skills_repository.find_by_identifier(identifier)

        if skill is None:
            return ResourNotFoundError(
                message="Usuário não encontrado.", resource="Usuário"
            )

        result = self.__skills_repository.delete(skill.get_identifier())

        if result is False:
            return ErrorServer(message="Erro ao tentar atualizar banco de dados.")

        return None
