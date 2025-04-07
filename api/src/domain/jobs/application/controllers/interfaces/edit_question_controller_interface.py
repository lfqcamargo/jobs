from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


class EditQuestionControllerInterface(ABC):
    """
    Interface for question editing controllers.

    This class defines the contract that any implementation of a question editing controller
    must follow. It provides a method to handle question update requests.

    Methods:
        handle(identifier: int, date_time: Optional[datetime], question_type:
        Optional[QuestionType],
        question: Optional[str], response: Optional[str]) -> None:
            Handles the question editing logic.
    """

    @abstractmethod
    def handle(
        self,
        identifier: int,
        date_time: Optional[datetime],
        question_type: Optional[QuestionTypes],
        question: Optional[str],
        response: Optional[str],
    ) -> None:
        """
        Handles the question editing logic.

        Args:
            identifier (int): Identifier of the question to be edited.
            date_time (Optional[datetime]): New date and time of the question.
            question_type (Optional[QuestionType]): New question type.
            question (Optional[str]): New question text.
            response (Optional[str]): New response text.

        Raises:
            ResourceNotFoundError: If the question does not exist in the system.
            DomainError: For any unexpected domain-related errors.

        Returns:
            None: If the edit is successful.
        """
