from src.domain.users.application.controllers.interfaces.delete_skill_controller_interface import (
    DeleteSkillControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.delete_skill_validator import delete_skill_validator


class DeleteSkillView(ViewInterface):
    """
    View responsible for handling HTTP requests related to skill deletion.

    This class acts as an adapter between HTTP requests and the
    DeleteSkillControllerInterface, ensuring proper request validation
    and response formatting.
    """

    def __init__(self, controller: DeleteSkillControllerInterface) -> None:
        """
        Initializes the DeleteSkillView with a specific controller.

        Args:
            controller (DeleteSkillControllerInterface): The controller
            responsible for handling skill
            deletion requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        delete_skill_validator(http_request)
        skill_id = http_request.params["identifier"]

        self.__controller.handle(identifier=skill_id)

        return HttpResponse(status_code=204, body=None)
