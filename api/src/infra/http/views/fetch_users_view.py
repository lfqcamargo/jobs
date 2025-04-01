from src.domain.users.application.controllers.interfaces.fetch_users_controller_interface import (
    FetchUsersControllerInterface,
)
from src.infra.presenters.user_presenter import UserPresenter
from src.infra.http.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class FetchUsersView(ViewInterface):
    """
    View responsible for handling HTTP requests related to fetching users.

    This class acts as an adapter between HTTP requests and the
    FetchUsersControllerInterface, ensuring proper request handling and response formatting.
    """

    def __init__(self, controller: FetchUsersControllerInterface) -> None:
        """
        Initializes the FetchUsersView with a specific controller.

        Args:
            controller (FetchUsersControllerInterface): The controller responsible for handling user
            fetch requests.
        """
        self.__controller = controller

    def handle(self, _) -> HttpResponse:
        users_data = self.__controller.handle()

        return HttpResponse(
            status_code=200,
            body={"users": list(map(UserPresenter.to_http, users_data))},
        )
