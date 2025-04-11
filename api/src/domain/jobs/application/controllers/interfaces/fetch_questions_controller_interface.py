from abc import ABC, abstractmethod
from typing import Union, Optional
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.enterprise.entities.question import Question


class FetchQuestionsControllerInterface(ABC):
    """
    Interface for question fetching controllers.

    This defines the contract that any implementation of a question-fetching controller must follow.
    """

    @abstractmethod
    def handle(
        self, user_id: int, company_id: Optional[int] = None
    ) -> Union[list[Question], ResourceNotFoundError]:
        """
        Handles the logic to fetch all questions associated with a user, optionally filtered
        by company.

        Args:
            user_id (int): The identifier of the user.
            company (Optional[int], optional): The identifier of the company to further
            filter the questions.

        Returns:
            list[Question]: A list of Question entities.
            ResourceNotFoundError: If no questions are found for the user.
        """
