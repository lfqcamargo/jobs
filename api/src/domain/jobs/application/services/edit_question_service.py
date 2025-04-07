from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from ..interfaces.questions_repository_interface import QuestionsRepositoryInterface
from ..dto.edit_question_dto import EditQuestionDTO


class EditQuestionService:
    """
    Service responsible for updating question data.

    This class ensures that a question exists before updating its details.
    """

    def __init__(
        self,
        questions_repository: QuestionsRepositoryInterface,
    ) -> None:
        """
        Initializes the EditQuestionService with a questions repository.

        Args:
            questions_repository (QuestionsRepositoryInterface): Repository for
            question-related operations.
        """
        self.__questions_repository = questions_repository

    def execute(self, props: EditQuestionDTO) -> None:
        """
        Executes the question update process.

        This method verifies if the question exists and updates its details accordingly.
        If the question is not found, returns a `ResourceNotFoundError`.
        If there is an error during the update, returns a `DomainError`.

        Args:
            props (EditQuestionDTO): Data transfer object containing the updated question details.

        Returns:
            None | ResourceNotFoundError | DomainError
        """
        question = self.__questions_repository.find_by_identifier(props.identifier)

        if question is None:
            return ResourceNotFoundError(
                message="Pergunta não encontrada.", resource="Pergunta"
            )

        if props.date_time is not None:
            question.set_date_time(props.date_time)

        if props.question_type is not None:
            question.set_question_type(props.question_type)

        if props.question is not None:
            question.set_question(props.question)

        if props.response is not None:
            question.set_response(props.response)

        result = self.__questions_repository.save(question)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
