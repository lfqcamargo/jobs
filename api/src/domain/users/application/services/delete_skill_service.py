from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.error_server import ErrorServer
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface


class DeleteSkillService:
    """
    Service responsible for handling skill deletion.

    This class ensures that a skill exists before attempting to delete it.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initialize the DeleteSkillService with a skills repository.

        Args:
            skills_repository (SkillsRepositoryInterface): Repository for skill-related operations.
        """
        self.__skills_repository = skills_repository

    def execute(self, identifier: int) -> None:
        """
        Execute the skill deletion process.

        Verifies if the skill exists before deleting it.
        If the skill does not exist, returns a `ResourceNotFoundError`.
        If there is an error during deletion, returns an `ErrorServer`.

        Args:
            identifier (int): The identifier of the skill to be deleted.

        Returns:
            None | ResourceNotFoundError | ErrorServer
        """
        skill = self.__skills_repository.find_by_identifier(identifier)

        if skill is None:
            return ResourceNotFoundError(
                message="Habilidade não encontrada.", resource="Habilidade"
            )

        result = self.__skills_repository.delete(skill.get_identifier())

        if result is False:
            return ErrorServer(message="Erro ao tentar atualizar banco de dados.")

        return None
