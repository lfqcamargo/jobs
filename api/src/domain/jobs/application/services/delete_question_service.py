from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from ..interfaces.questions_repository_interface import QuestionsRepositoryInterface


class DeleteQuestionService:
    """
    Service responsible for handling question deletion.

    This class ensures that a question exists before attempting to delete it.
    """

    def __init__(
        self,
        questions_repository: QuestionsRepositoryInterface,
    ) -> None:
        """
        Initialize the DeleteQuestionService with a questions repository.

        Args:
            questions_repository (QuestionsRepositoryInterface): Repository for
            question-related operations.
        """
        self.__questions_repository = questions_repository

    def execute(self, identifier: int) -> None:
        """
        Execute the question deletion process.

        Verifies if the question exists before deleting it.
        If the question does not exist, returns a `ResourceNotFoundError`.
        If there is an error during deletion, returns a `DomainError`.

        Args:
            identifier (int): The identifier of the question to be deleted.

        Returns:
            None | ResourceNotFoundError | DomainError
        """
        question = self.__questions_repository.find_by_identifier(identifier)

        if question is None:
            return ResourceNotFoundError(
                message="Pergunta não encontrada.", resource="Pergunta"
            )

        result = self.__questions_repository.delete(question.get_identifier())

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
