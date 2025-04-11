from src.domain.jobs.enterprise.enums.question_types import QuestionTypes
from src.domain.jobs.application.controllers.interfaces.edit_question_controller_interface import (
    EditQuestionControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.edit_question_validator import edit_question_validator


class EditQuestionView(ViewInterface):
    """
    View responsible for handling HTTP requests related to editing questions.

    This class acts as an adapter between HTTP requests and the
    EditQuestionControllerInterface, ensuring proper request validation
    and response formatting.
    """

    def __init__(self, controller: EditQuestionControllerInterface) -> None:
        """
        Initializes the EditQuestionView with a specific controller.

        Args:
            controller (EditQuestionControllerInterface): The controller responsible
            for handling question editing requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the incoming HTTP request to edit a question.

        Args:
            http_request (HttpRequest): The HTTP request containing the necessary data
            to edit the question.

        Returns:
            HttpResponse: The HTTP response indicating the result of the operation.
        """
        edit_question_validator(http_request)

        identifier = http_request.params["identifier"]
        date_time = http_request.body.get("date_time", None)
        question = http_request.body.get("question", None)
        response = http_request.body.get("response", None)
        question_type = http_request.body.get("question_type", None)

        if question_type:
            question_type = QuestionTypes(question_type)

        body_response = self.__controller.handle(
            identifier=identifier,
            date_time=date_time,
            question=question,
            response=response,
            question_type=question_type,
        )

        return HttpResponse(status_code=200, body=body_response)
