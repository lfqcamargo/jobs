from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.domain.users.application.services.edit_user_service import EditUserService
from src.domain.users.application.controllers.edit_user_controller import (
    EditUserController,
)
from src.infra.http.views.edit_user_view import EditUserView
from src.infra.drivers.password_handler import PasswordHandler


def edit_user_composer() -> EditUserView:
    """
    Composer function to create and return an EditUserView instance.

    This function initializes the necessary dependencies for editing user data,
    including the UsersRepository, PasswordHandler, EditUserService, EditUserController,
    and EditUserView. It ties all components together to create a complete
    view that can handle user editing requests.

    Returns:
        EditUserView: The initialized EditUserView instance, ready to handle HTTP requests.
    """
    password_handler = PasswordHandler()
    users_repository = UsersRepository(db_connection_handler)
    service = EditUserService(users_repository, password_handler)
    controller = EditUserController(service)
    view = EditUserView(controller)

    return view
