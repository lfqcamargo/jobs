from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import (
    UsersRepository,
)
from src.infra.desktop.controllers.create_user_controller import (
    CreateUserController,
)
from src.domain.users.application.services.create_user_service import (
    CreateUserService,
)
from src.infra.drivers.password_handler import PasswordHandler


def create_user_composer() -> CreateUserController:
    """
    Composer function to create and return a CreateUserController instance.

    This function initializes the necessary dependencies for user creation,
    including the UsersRepository, CreateUserService, CreateUserController,
    and CreateUserController. It ties all components together to create a complete
    view that can handle user creation requests.

    Returns:
        CreateUserController: The initialized CreateUserController instance.
    """
    password_handler = PasswordHandler()
    users_repository = UsersRepository(db_connection_handler)
    service = CreateUserService(users_repository, password_handler)
    controller = CreateUserController(service)

    return controller
