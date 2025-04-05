from src.domain.users.application.controllers.interfaces.edit_skill_controller_interface import (
    EditSkillControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.edit_skill_validator import edit_skill_validator
from src.domain.users.enterprise.enums.skill_level import SkillLevel


class EditSkillView(ViewInterface):
    """
    View responsible for handling HTTP requests related to skill editing.

    This class acts as an adapter between HTTP requests and the
    EditSkillControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: EditSkillControllerInterface) -> None:
        """
        Initializes the EditSkillView with a specific controller.

        Args:
            controller (EditSkillControllerInterface): The controller responsible for handling skill
            editing requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        edit_skill_validator(http_request)

        identifier = http_request.params["identifier"]
        description = http_request.body.get("description", None)
        time_month = http_request.body.get("time_month", None)
        level = http_request.body.get("level", None)

        if level:
            level = SkillLevel(level)

        body_response = self.__controller.handle(
            identifier=identifier,
            description=description,
            time_month=time_month,
            level=level,
        )

        return HttpResponse(status_code=200, body=body_response)
