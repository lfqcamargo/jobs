from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.domain.users.application.services.fetch_users_service import FetchUsersService


def fetch_users_composer() -> FetchUsersService:
    """
    Composer function to create and return a FetchUsersService instance.

    This function initializes the necessary dependencies for fetching users,
    including the UsersRepository and FetchUsersService. It ties these components
    together to provide a service responsible for fetching users.

    Returns:
        FetchUsersService: The initialized FetchUsersService instance, ready to be
        executed to fetch users from the repository.
    """
    users_repository = UsersRepository(db_connection_handler)
    service = FetchUsersService(users_repository)

    return service
