from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import (
    UsersRepository,
)
from src.domain.users.application.controllers.delete_user_controller import (
    DeleteUserController,
)
from src.infra.http.views.delete_user_view import DeleteUserView
from src.domain.users.application.services.delete_user_service import (
    DeleteUserService,
)


def delete_user_composer() -> DeleteUserView:
    """
    Composer function to create and return a DeleteUserView instance.

    This function initializes the necessary dependencies for user deletion,
    including the UsersRepository, DeleteUserService, DeleteUserController,
    and DeleteUserView. It ties all components together to create a complete
    view that can handle user deletion requests.

    Returns:
        DeleteUserView: The initialized DeleteUserView instance, ready to handle HTTP requests.
    """
    users_repository = UsersRepository(db_connection_handler)
    service = DeleteUserService(users_repository)
    controller = DeleteUserController(service)
    view = DeleteUserView(controller)

    return view
