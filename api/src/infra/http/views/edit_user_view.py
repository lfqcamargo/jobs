from datetime import datetime
from src.domain.users.application.controllers.interfaces.edit_user_controller_interface import (
    EditUserControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.edit_user_validator import edit_user_validator


class EditUserView(ViewInterface):
    """
    View responsible for handling HTTP requests related to user editing.

    This class acts as an adapter between HTTP requests and the
    EditUserControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: EditUserControllerInterface) -> None:
        """
        Initializes the EditUserView with a specific controller.

        Args:
            controller (EditUserControllerInterface): The controller responsible for handling user
            editing requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        edit_user_validator(http_request)

        identifier = http_request.params["id"]
        name = http_request.body.get("name", None)
        email = http_request.body.get("email", None)
        password = http_request.body.get("password", None)
        birthday_date_str = http_request.body.get("birthday_date", None)

        birthday_date = None
        if birthday_date_str:
            birthday_date = datetime.strptime(birthday_date_str, "%d/%m/%Y").date()

        curriculum = http_request.files.get("curriculum", None)

        if curriculum:
            curriculum = curriculum.read()

        body_response = self.__controller.handle(
            identifier=identifier,
            name=name,
            email=email,
            password=password,
            birthday_date=birthday_date,
            curriculum=curriculum,
        )

        return HttpResponse(status_code=201, body=body_response)
