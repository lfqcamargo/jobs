from src.domain.jobs.application.controllers.interfaces.run_linkedin_controller_interface import (
    RunLinkedinControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class RunLinkedinView(ViewInterface):
    """
    View responsible for handling HTTP requests related to run linkedin.

    This class acts as an adapter between HTTP requests and the
    RunLinkedinControllerInterface, ensuring proper request handling and response formatting.
    """

    def __init__(self, controller: RunLinkedinControllerInterface) -> None:
        """
        Initializes the RunLinkedinView with a specific controller.

        Args:
            controller (RunLinkedinControllerInterface): The controller responsible for handling run
            linkedin.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        user_id = http_request.params["user_id"]
        body_response = self.__controller.handle(user_id)

        return HttpResponse(status_code=200, body=body_response)
