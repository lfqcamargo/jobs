from src.domain.users.application.controllers.interfaces.fetch_skills_controller_interface import (
    FetchSkillsControllerInterface,
)
from src.infra.presenters.skill_presenter import SkillPresenter
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.fetch_skills_validator import fetch_skills_validator


class FetchSkillsView(ViewInterface):
    """
    View responsible for handling HTTP requests related to fetching user skills.

    This class acts as an adapter between HTTP requests and the
    FetchSkillsControllerInterface, ensuring proper request handling and response formatting.
    """

    def __init__(self, controller: FetchSkillsControllerInterface) -> None:
        """
        Initializes the FetchSkillsView with a specific controller.

        Args:
            controller (FetchSkillsControllerInterface): The controller responsible
            for handling skill
            fetch requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        fetch_skills_validator(http_request)

        user_id = http_request.params["user_id"]
        skills_data = self.__controller.handle(user_id=user_id)

        return HttpResponse(
            status_code=200,
            body={"skills": list(map(SkillPresenter.to_http, skills_data))},
        )
