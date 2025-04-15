from datetime import datetime
from src.domain.users.application.controllers.interfaces.create_user_controller_interface import (
    CreateUserControllerInterface,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..validators.create_user_validator import create_user_validator
from werkzeug.datastructures import FileStorage


class CreateUserView(ViewInterface):
    """
    View responsible for handling HTTP requests related to user creation.

    This class acts as an adapter between HTTP requests and the
    CreateUserControllerInterface, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: CreateUserControllerInterface) -> None:
        """
        Initializes the CreateUserView with a specific controller.

        Args:
            controller (CreateUserControllerInterface): The controller responsible for handling user
            creation requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_user_validator(http_request)

        birthday_date = datetime.strptime(
            http_request.body["birthday_date"], "%d/%m/%Y"
        ).date()

        name = http_request.body["name"]
        email = http_request.body["email"]
        password = http_request.body["password"]
        country_code = http_request.body["country_code"]
        phone_number = http_request.body["phone_number"]
        curriculum: FileStorage = http_request.files

        curriculum = http_request.files.read()

        body_response = self.__controller.handle(
            name=name,
            email=email,
            password=password,
            birthday_date=birthday_date,
            curriculum=curriculum,
            country_code=country_code,
            phone_number=phone_number,
        )

        return HttpResponse(status_code=201, body=body_response)
