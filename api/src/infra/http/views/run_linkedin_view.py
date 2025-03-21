from src.infra.http.controllers.run_linkedin_controller import (
    RunLinkedinController,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.run_linkedin_validator import validate_request_params


class RunLinkedinView(ViewInterface):
    """
    View responsible for handling HTTP requests related to fetching companies.

    This class acts as an adapter between HTTP requests and the
    RunLinkedinController, ensuring proper request handling and response formatting.
    """

    def __init__(self, controller: RunLinkedinController) -> None:
        """
        Initializes the RunLinkedinView with a specific controller.

        Args:
            controller (RunLinkedinController): The controller responsible for handling the
            request logic.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        validate_request_params(http_request)

        email = http_request.param
        body_response = self.__controller.handle(email)
        return HttpResponse(status_code=200, body=body_response)
