from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.jobs.application.services.delete_question_service import (
    DeleteQuestionService,
)
from .interfaces.delete_question_controller_interface import (
    DeleteQuestionControllerInterface,
)


class DeleteQuestionController(DeleteQuestionControllerInterface):
    """
    Controller responsible for handling question deletion requests.

    This controller coordinates the question deletion process. It communicates with the
    service layer
    to perform the actual deletion logic. It raises relevant exceptions if errors are encountered,
    such as when a question is not found or when domain-related errors occur.

    Methods:
        handle(identifier: int) -> None:
            Handles the question deletion process.
    """

    def __init__(self, service: DeleteQuestionService) -> None:
        """
        Initializes the DeleteQuestionController with a question service.

        Args:
            service (DeleteQuestionService): The service handling question deletion logic.
        """
        self.__service = service

    def handle(self, identifier: int) -> None:
        result = self.__service.execute(identifier)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
