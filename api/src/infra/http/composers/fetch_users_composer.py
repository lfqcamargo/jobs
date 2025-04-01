from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.domain.users.application.services.fetch_users_service import FetchUsersService
from src.domain.users.application.controllers.fetch_users_controller import (
    FetchUsersController,
)
from src.infra.http.views.fetch_users_view import FetchUsersView
from src.infra.database.postgres.settings.connection import db_connection_handler


def fetch_users_composer() -> FetchUsersView:
    """
    Composer function to create and return a FetchUsersView instance.

    This function initializes the necessary dependencies for fetching users,
    including the UsersRepository, FetchUsersService, FetchUsersController,
    and FetchUsersView. It ties all components together to create a complete
    view that can handle user fetching requests.

    Returns:
        FetchUsersView: The initialized FetchUsersView instance, ready to handle HTTP requests.
    """
    users_repository = UsersRepository(db_connection_handler)
    service = FetchUsersService(users_repository)
    controller = FetchUsersController(service)
    view = FetchUsersView(controller)

    return view
