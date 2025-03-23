from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import (
    UsersRepository,
)
from src.infra.desktop.controllers.edit_user_controller import (
    EditUserController,
)
from src.domain.users.application.services.edit_user_service import (
    EditUserService,
)
from src.infra.drivers.password_handler import PasswordHandler


def edit_user_composer() -> EditUserController:
    """
    Composer function to initialize and return an instance of EditUserController.

    This function sets up all the necessary components for editing a user's information,
    including the repository, service, password handler, and the controller.
    It assembles these components together and returns an EditUserController that
    can handle user edit requests.

    Returns:
        EditUserController: The initialized EditUserController instance, ready to
        handle user edit operations.
    """
    password_handler = PasswordHandler()
    users_repository = UsersRepository(db_connection_handler)
    service = EditUserService(users_repository, password_handler)
    controller = EditUserController(service)

    return controller
