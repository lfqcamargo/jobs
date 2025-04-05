from src.domain.users.application.controllers.interfaces.create_skill_controller_interface import (
    CreateSkillControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.create_skill_validator import create_skill_validator


class CreateSkillView(ViewInterface):
    """
    View responsible for handling HTTP requests related to skill creation.

    This class acts as an adapter between HTTP requests and the
    CreateSkillControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: CreateSkillControllerInterface) -> None:
        """
        Initializes the CreateSkillView with a specific controller.

        Args:
            controller (CreateSkillControllerInterface): The controller responsible
            for handling skill
            creation requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the incoming HTTP request to create a skill.

        Args:
            http_request (HttpRequest): The HTTP request containing skill data.

        Returns:
            HttpResponse: The HTTP response indicating the result of the operation.
        """
        create_skill_validator(http_request)

        description = http_request.body["description"]
        time_month = http_request.body["time_month"]
        level = http_request.body["level"]
        user_id = int(http_request.params["user_id"])

        body_response = self.__controller.handle(
            description=description, time_month=time_month, level=level, user_id=user_id
        )

        return HttpResponse(status_code=201, body=body_response)
