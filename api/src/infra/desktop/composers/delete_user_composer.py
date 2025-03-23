from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import (
    UsersRepository,
)
from src.infra.desktop.controllers.delete_user_controller import (
    DeleteUserController,
)
from src.domain.users.application.services.delete_user_service import (
    DeleteUserService,
)


def delete_user_composer() -> DeleteUserController:
    """
    Composer function to initialize and return a DeleteUserController instance.

    This function orchestrates the creation of all necessary dependencies for the
    user deletion process. It initializes the UsersRepository, DeleteUserService,
    and DeleteUserController, and ties them together to provide a complete controller
    capable of handling user deletion requests.

    Returns:
        DeleteUserController: The initialized DeleteUserController instance, which can
        be used to handle user deletion logic.
    """
    users_repository = UsersRepository(db_connection_handler)
    service = DeleteUserService(users_repository)
    controller = DeleteUserController(service)

    return controller
