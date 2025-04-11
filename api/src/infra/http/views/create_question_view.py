from src.domain.jobs.application.controllers.interfaces.create_question_controller_interface import (
    CreateQuestionControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.create_question_validator import create_question_validator


class CreateQuestionView(ViewInterface):
    """
    View responsible for handling HTTP requests related to question creation.

    This class acts as an adapter between HTTP requests and the
    CreateQuestionControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: CreateQuestionControllerInterface) -> None:
        """
        Initializes the CreateQuestionView with a specific controller.

        Args:
            controller (CreateQuestionControllerInterface): The controller responsible
            for handling question creation requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the incoming HTTP request to create a question.

        Args:
            http_request (HttpRequest): The HTTP request containing question data.

        Returns:
            HttpResponse: The HTTP response indicating the result of the operation.
        """
        create_question_validator(http_request)

        company_id = int(http_request.params["company_id"])
        user_id = int(http_request.params["user_id"])
        date_time = http_request.body["date_time"]
        question_text = http_request.body["question"]
        response_text = http_request.body["response"]
        question_type = http_request.body["question_type"]

        body_response = self.__controller.handle(
            company_id=company_id,
            user_id=user_id,
            date_time=date_time,
            question=question_text,
            response=response_text,
            question_type=question_type,
        )

        return HttpResponse(status_code=201, body=body_response)
