from typing import Optional
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.enterprise.entities.question import Question
from src.domain.jobs.application.services.fetch_questions_service import (
    FetchQuestionsService,
)
from .interfaces.fetch_questions_controller_interface import (
    FetchQuestionsControllerInterface,
)


class FetchQuestionsController(FetchQuestionsControllerInterface):
    """
    Controller responsible for handling question fetching requests.

    Delegates the operation to the FetchQuestionsService and returns the result or error.
    """

    def __init__(self, service: FetchQuestionsService) -> None:
        """
        Initializes the controller with the fetch questions service.

        Args:
            service (FetchQuestionsService): Service layer handling the logic.
        """
        self.__service = service

    def handle(self, user_id: int, company_id: Optional[int] = None) -> list[Question]:
        """
        Executes the fetch operation via the service.

        Args:
            user_id (int): Identifier of the user whose questions are being fetched.
            company (Optional[int], optional): Company filter for the questions.

        Returns:
            list[Question]: If questions are found.

        Raises:
            ResourceNotFoundError: If no questions exist for the user.
        """
        result = self.__service.execute(user_id=user_id, company_id=company_id)

        if isinstance(result, ResourceNotFoundError):
            raise result

        return result
