from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
from ..interfaces.skills_repository_interface import SkillsRepositoryInterface
from ..dto.edit_skill_dto import EditSkillDTO


class EditSkillService:
    """
    Service responsible for editing skill data.

    This class handles the business logic for updating an existing skill's data,
    ensuring that the provided email does not conflict with another skill's email.

    Attributes:
        __skills_repository (SkillsRepositoryInterface): Repository for skill data operations.
    """

    def __init__(
        self,
        skills_repository: SkillsRepositoryInterface,
    ) -> None:
        """
        Initializes the EditSkillService with a skill repository and password handler.

        Args:
            skills_repository (SkillsRepositoryInterface): The repository responsible for skill
            data operations.
            password_handler (PasswordHandlerInterface): The handler responsible for encrypting
            skill passwords.
        """
        self.__skills_repository = skills_repository

    def execute(self, props: EditSkillDTO) -> None:
        """
        Executes the skill data editing process.

        This method verifies if the skill exists, checks for any email conflicts,
        and updates the skill's details. It also updates the password if provided.

        Args:
            props (EditSkillDTO): The data transfer object containing the skill details to be
            updated.
        Returns:
            None
        """

        skill = self.__skills_repository.find_by_identifier(props.identifier)

        if skill is None:
            raise ResourNotFoundError(
                "Habilidade não encontrado.", resource="Habilidade"
            )

        skill.set_
        skill.set_name(props.name)
        skill.set_birthday_date(props.birthday_date)

        result = self.__skills_repository.save(skill)

        if result is False:
            return ErrorServer(message="Erro ao tentar atualizar banco de dados.")

        return None
