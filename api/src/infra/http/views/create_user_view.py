from src.infra.http.controllers.create_user_controller import (
    CreateUserController,
)
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from src.domain.users.application.dto.create_user_dto import CreateUserDTO
from .interfaces.view_interface import ViewInterface
from ..validators.create_user_validator import create_user_validator


class CreateUserView(ViewInterface):
    """
    View responsible for handling HTTP requests related to user creation.

    This class acts as an adapter between HTTP requests and the
    CreateUserController, ensuring proper request validation and response formatting.
    """

    def __init__(self, controller: CreateUserController) -> None:
        """
        Initializes the CreateUserView with a specific controller.

        Args:
            controller (CreateUserController): The controller responsible for handling user
            creation requests.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_user_validator(http_request)

        dto = CreateUserDTO(
            name=http_request.name,
            email=http_request.email,
            password=http_request.password,
            birthday_date=http_request.birthday_date,
        )

        body_response = self.__controller.handle(dto)
        return HttpResponse(status_code=201, body=body_response)
