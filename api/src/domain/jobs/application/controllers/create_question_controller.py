from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.jobs.application.services.create_question_service import (
    CreateQuestionService,
)
from src.domain.jobs.application.dto.create_question_dto import CreateQuestionDTO
from .interfaces.create_question_controller_interface import (
    CreateQuestionControllerInterface,
)
from datetime import datetime
from typing import Optional
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


class CreateQuestionController(CreateQuestionControllerInterface):
    """
    Controller responsible for handling question creation requests.

    This controller coordinates the question creation process. It communicates with the service
    layer
    to perform the actual creation logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when a user or company is not found,
    or when domain-related errors occur.

    Methods:
        handle(company_id, user_id, date_time, question_type, question, response, identifier)
        -> None:
            Handles the question creation process by calling the service layer with the
            provided question data. If any errors occur, they are raised appropriately.

    Raises:
        ResourceNotFoundError: If the user or company is not found.
        DomainError: For any unexpected domain-related errors.
    """

    def __init__(self, service: CreateQuestionService) -> None:
        """
        Initializes the CreateQuestionController with a question service.

        Args:
            service (CreateQuestionService): The service handling question creation logic.
        """
        self.__service = service

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
        dto = CreateQuestionDTO(
            company_id=company_id,
            user_id=user_id,
            date_time=date_time,
            question_type=question_type,
            question=question,
            response=response,
            identifier=identifier,
        )

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
