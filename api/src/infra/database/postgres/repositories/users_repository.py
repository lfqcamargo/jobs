from src.domain.users.application.interfaces.users_repository_interface import (
    UsersRepositoryInterface,
)
from src.domain.users.enterprise.entities.user import User

from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.infra.database.postgres.models.user_model import UserModel
from src.infra.database.postgres.mappers.user_mapper import UserMapper


class UsersRepository(UsersRepositoryInterface):
    """
    Repository class for managing User data in a PostgreSQL database.

    This class implements the UsersRepositoryInterface and provides methods
    to retrieve user records from the database.
    """

    def __init__(self, db_connection: DBConnectionHandlerInterface) -> None:
        self.__db_connection = db_connection

    def find_by_email(self, email: str) -> User | None:
        with self.__db_connection as database:
            user_model = (
                database.session.query(UserModel)
                .filter(UserModel.email == email)
                .first()
            )
            if user_model:
                return UserMapper.to_domain(user_model)
            return None
