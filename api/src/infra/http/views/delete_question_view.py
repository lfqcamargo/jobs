from src.domain.jobs.application.controllers.interfaces.delete_question_controller_interface import (
    DeleteQuestionControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.delete_question_validator import delete_question_validator


class DeleteQuestionView(ViewInterface):
    """
    View responsible for handling HTTP requests related to deleting questions.

    This class acts as an adapter between HTTP requests and the
    DeleteQuestionControllerInterface, ensuring proper request validation
    and response formatting.
    """

    def __init__(self, controller: DeleteQuestionControllerInterface) -> None:
        """
        Initializes the DeleteQuestionView with a specific controller.

        Args:
            controller (DeleteQuestionControllerInterface): The controller responsible
            for handling question deletion requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the incoming HTTP request to delete a question.

        Args:
            http_request (HttpRequest): The HTTP request containing the necessary parameters
            to delete the question.

        Returns:
            HttpResponse: The HTTP response indicating the result of the operation.
        """
        delete_question_validator(http_request)
        question_id = http_request.params["identifier"]

        self.__controller.handle(identifier=question_id)

        return HttpResponse(status_code=204, body=None)
