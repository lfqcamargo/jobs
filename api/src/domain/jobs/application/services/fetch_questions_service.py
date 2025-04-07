from src.core.errors.resource_not_found_error import ResourceNotFoundError
from ..interfaces.questions_repository_interface import QuestionsRepositoryInterface
from ...enterprise.entities.question import Question


class FetchQuestionsService:
    """
    Service responsible for retrieving all questions associated with a user.

    This service fetches questions from the repository, ensuring the data is consistent.
    If no questions are found for the user, an error is raised.
    """

    def __init__(
        self,
        questions_repository: QuestionsRepositoryInterface,
    ) -> None:
        """
        Initializes the FetchQuestionsService with a questions repository.

        Args:
            questions_repository (QuestionsRepositoryInterface): The repository responsible for
            retrieving question data.

        Returns:
            None
        """
        self.__questions_repository = questions_repository

    def execute(self, user_id: int) -> list[Question] | ResourceNotFoundError:
        """
        Retrieves the list of questions for a specific user.

        This method fetches the questions associated with the provided user ID and
        returns them. If no questions are found for the user, a `ResourceNotFoundError` is raised.

        Args:
            user_id (int): The identifier of the user for whom questions should be fetched.

        Returns:
            list[Question]: A list of `Question` objects associated with the given user.

        Raises:
            ResourceNotFoundError: If no questions are found for the specified user.
        """
        questions = self.__questions_repository.fetch_all_by_user(user_id)

        if not questions:
            return ResourceNotFoundError(
                message="Perguntas não encontradas.", resource="Perguntas"
            )

        return questions
