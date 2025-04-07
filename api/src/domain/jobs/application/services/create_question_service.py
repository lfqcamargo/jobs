from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.interfaces.users_repository_interface import (
    UsersRepositoryInterface,
)
from ..interfaces.questions_repository_interface import QuestionsRepositoryInterface
from ..dto.create_question_dto import CreateQuestionDTO
from ...enterprise.entities.question import Question


class CreateQuestionService:
    """
    Service responsible for handling question creation logic.

    This class ensures that a question is created only if the associated user exists.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
        questions_repository: QuestionsRepositoryInterface,
    ) -> None:
        """
        Initialize the CreateQuestionService with user and question repositories.

        Args:
            users_repository (UsersRepositoryInterface): Repository for user-related operations.
            questions_repository (QuestionsRepositoryInterface): Repository for question-related
            operations.
        """
        self.__users_repository = users_repository
        self.__questions_repository = questions_repository

    def execute(self, props: CreateQuestionDTO) -> None:
        """
        Execute the question creation process.

        Ensures that the user exists before creating a new question.
        If the user does not exist, returns a `ResourceNotFoundError`.
        If there is an error while saving the question, returns a `DomainError`.

        Args:
            props (CreateQuestionDTO): The DTO containing question details.

        Returns:
            None | ResourceNotFoundError | DomainError
        """
        user_identifier = self.__users_repository.find_by_identifier(props.user_id)

        if user_identifier is None:
            return ResourceNotFoundError(
                message="Usuário não cadastrado.", resource="Usuário"
            )

        question = Question.create(props)
        result = self.__questions_repository.create(question)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
