from src.domain.users.application.services.fetch_users_service import FetchUsersService

from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from ..controllers.fetch_users_controller import FetchUserController


def fetch_users_composer() -> FetchUserController:
    """
    Composer function to create and return a FetchUserController instance.

    This function initializes the necessary dependencies for fetching users,
    including the UsersRepository and FetchUserController. It ties these components
    together to provide a service responsible for fetching users.

    Returns:
        FetchUserController: The initialized FetchUserController instance, ready to be
        executed to fetch users from the repository.
    """
    users_repository = UsersRepository(db_connection_handler)
    service = FetchUsersService(users_repository)
    controller = FetchUserController(service)

    return controller
