from typing import Optional
from datetime import datetime
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.jobs.application.services.edit_question_service import (
    EditQuestionService,
)
from src.domain.jobs.application.dto.edit_question_dto import EditQuestionDTO
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes
from .interfaces.edit_question_controller_interface import (
    EditQuestionControllerInterface,
)


class EditQuestionController(EditQuestionControllerInterface):
    """
    Controller responsible for handling question editing requests.

    This controller coordinates the question editing process. It communicates with the service layer
    to perform the update logic. It raises relevant exceptions if errors are encountered,
    such as when a question is not found or when domain-related errors occur.
    """

    def __init__(self, service: EditQuestionService) -> None:
        """
        Initializes the EditQuestionController with a question service.

        Args:
            service (EditQuestionService): The service handling question editing logic.
        """
        self.__service = service

    def handle(
        self,
        identifier: int,
        date_time: Optional[datetime],
        question_type: Optional[QuestionTypes],
        question: Optional[str],
        response: Optional[str],
    ) -> None:
        dto = EditQuestionDTO(
            identifier=identifier,
            date_time=date_time,
            question=question,
            response=response,
            question_type=question_type,
        )

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
