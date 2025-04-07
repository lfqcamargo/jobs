from typing import Optional
from datetime import datetime
from abc import ABC, abstractmethod
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


class CreateQuestionControllerInterface(ABC):
    """
    Interface for the question creation controllers.

    This class defines the contract that any implementation of a question creation controller
    must follow. It provides a method to handle question creation requests.

    Methods:
        handle(user_id: str, content: str) -> None:
            Handles the question creation logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(
        self,
        company_id: int,
        user_id: int,
        date_time: datetime,
        question_type: QuestionTypes,
        question: str,
        response: Optional[str] = None,
        identifier: int = 0,
    ) -> None:
        """
        Handles the question creation logic.

        Args:
            company_id (int): ID of the company related to the question.
            user_id (int): ID of the user who is creating the question.
            date_time (datetime): Date and time of the question.
            question_type (QuestionTypes): Type of the question.
            question (str): The question content.
            response (Optional[str], optional): The response to the question, if any. Defaults to
            None.
            identifier (int, optional): The identifier for the question. Defaults to 0.

        Raises:
            ResourceNotFoundError: If the user or company does not exist.
            DomainError: For any unexpected domain-related errors.
        """
