from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ..dto.edit_skill_dto import EditSkillDTO


class EditSkillService:
    """
    Service responsible for updating skill data.

    This class ensures that a skill exists before updating its details.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initializes the EditSkillService with a skills repository.

        Args:
            skills_repository (SkillsRepositoryInterface): Repository for skill-related operations.
        """
        self.__skills_repository = skills_repository

    def execute(self, props: EditSkillDTO) -> None:
        """
        Executes the skill update process.

        This method verifies if the skill exists and updates its details accordingly.
        If the skill is not found, returns a `ResourceNotFoundError`.
        If there is an error during the update, returns an `DomainError`.

        Args:
            props (EditSkillDTO): Data transfer object containing the updated skill details.

        Returns:
            None | ResourceNotFoundError | DomainError
        """
        skill = self.__skills_repository.find_by_identifier(props.identifier)

        if skill is None:
            return ResourceNotFoundError(
                message="Habilidade não encontrada.", resource="Habilidade"
            )

        skill.set_description(props.description)
        skill.set_level(props.level)
        skill.set_time_month(props.time_month)

        result = self.__skills_repository.save(skill)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
