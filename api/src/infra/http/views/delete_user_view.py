from src.domain.users.application.controllers.interfaces.delete_user_controller_interface import (
    DeleteUserControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.delete_user_validator import delete_user_validator


class DeleteUserView(ViewInterface):
    """
    View responsible for handling HTTP requests related to user deletion.

    This class acts as an adapter between HTTP requests and the
    DeleteUserControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: DeleteUserControllerInterface) -> None:
        """
        Initializes the DeleteUserView with a specific controller.

        Args:
            controller (DeleteUserControllerInterface): The controller responsible for handling user
            deletion requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        delete_user_validator(http_request)
        user_id = http_request.params["identifier"]

        self.__controller.handle(identifier=user_id)

        return HttpResponse(status_code=204, body=None)
