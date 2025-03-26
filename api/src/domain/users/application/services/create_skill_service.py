from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ..dto.create_skill_dto import CreateSkillDTO
from ...enterprise.entities.skill import Skill


class CreateSkillService:
    """
    Service responsible for skill creation logic.

    This class handles the business logic for creating a new skill,
    ensuring that a skill with the given email does not already exist.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initializes the CreateSkillService with a skill repository.

        Args:
            skills_repository (SkillsRepositoryInterface): The repository responsible for
            skill data operations.
            password_handler (PasswordHandlerInterface): Driver to manage skill password.
        """
        self.__users_repository = users_repository
        self.__skills_repository = skills_repository

    def execute(self, props: CreateSkillDTO) -> None:
        """
        Executes the skill creation process.

        Checks if the email already exists; if not, creates a new skill.

        Args:
            props (CreateSkillDTO): The data transfer object containing skill details.

        Returns:
            None
        """
        user_identifier = self.__users_repository.find_by_identifier(
            props.idefind_by_identifier
        )

        if user_identifier is not None:
            raise ResourNotFoundError(
                message="Usuário não cadastrado.", resource="users"
            )

        skill = Skill.create(props)
        result = self.__skills_repository.create(skill)

        if result is False:
            return ErrorServer(message="Erro ao tentar atualizar banco de dados.")

        return None
