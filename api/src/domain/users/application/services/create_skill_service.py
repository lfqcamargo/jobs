from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ..dto.create_skill_dto import CreateSkillDTO
from ...enterprise.entities.skill import Skill


class CreateSkillService:
    """
    Service responsible for handling skill creation logic.

    This class ensures that a skill is created only if the associated user exists.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initialize the CreateSkillService with user and skill repositories.

        Args:
            users_repository (UsersRepositoryInterface): Repository for user-related operations.
            skills_repository (SkillsRepositoryInterface): Repository for skill-related operations.
        """
        self.__users_repository = users_repository
        self.__skills_repository = skills_repository

    def execute(self, props: CreateSkillDTO) -> None:
        """
        Execute the skill creation process.

        Ensures that the user exists before creating a new skill.
        If the user does not exist, returns a `ResourceNotFoundError`.
        If there is an error while saving the skill, returns an `DomainError`.

        Args:
            props (CreateSkillDTO): The DTO containing skill details.

        Returns:
            None | ResourceNotFoundError | DomainError
        """
        user_identifier = self.__users_repository.find_by_identifier(props.user_id)

        if user_identifier is None:
            return ResourceNotFoundError(
                message="Usuário não cadastrado.", resource="Usuário"
            )

        skill = Skill.create(props)
        result = self.__skills_repository.create(skill)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
