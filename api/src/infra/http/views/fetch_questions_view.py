from src.domain.jobs.application.controllers.interfaces.fetch_questions_controller_interface import (
    FetchQuestionsControllerInterface,
)
from src.infra.presenters.question_presenter import QuestionPresenter
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.fetch_questions_validator import fetch_questions_validator


class FetchQuestionsView(ViewInterface):
    """
    View responsible for handling HTTP requests related to fetching user questions.

    This class acts as an adapter between HTTP requests and the
    FetchQuestionsControllerInterface, ensuring proper request handling and response formatting.
    """

    def __init__(self, controller: FetchQuestionsControllerInterface) -> None:
        """
        Initializes the FetchQuestionsView with a specific controller.

        Args:
            controller (FetchQuestionsControllerInterface): The controller responsible
            for handling question fetch requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the incoming HTTP request to fetch questions for a user.

        Args:
            http_request (HttpRequest): The HTTP request containing the necessary data
            to fetch the questions.

        Returns:
            HttpResponse: The HTTP response containing the requested questions.
        """
        fetch_questions_validator(http_request)

        user_id = http_request.params["user_id"]
        company_id = http_request.params["company_id"]

        questions_data = self.__controller.handle(
            user_id=user_id, company_id=company_id
        )

        return HttpResponse(
            status_code=200,
            body={"questions": list(map(QuestionPresenter.to_http, questions_data))},
        )
