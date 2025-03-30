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

    def create(self, user: User) -> bool:
        with self.__db_connection as database:
            user_model = UserMapper.to_sql(user)
            try:
                database.session.add(user_model)
                database.session.commit()
                return True
            except Exception:
                return False

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

    def find_by_identifier(self, identifier: int) -> User | None:
        with self.__db_connection as database:
            user_model = (
                database.session.query(UserModel)
                .filter(UserModel.id == identifier)
                .first()
            )
            if user_model:
                return UserMapper.to_domain(user_model)
            return None

    def fetch_all(self) -> list[User] | None:
        with self.__db_connection as database:
            user_model = database.session.query(UserModel).all()
            if user_model:
                users = []
                for user in user_model:
                    users.append(UserMapper.to_domain(user))

                return users

            return None

    def save(self, user: User) -> bool:
        with self.__db_connection as database:

            user_model = UserMapper.to_sql(user)
            try:
                database.session.merge(user_model)
                database.session.commit()
                return True
            except Exception:
                return False

    def delete(self, identifier: int) -> bool:
        """
        Deletes a user by identifier from the database.

        Args:
            identifier (int): The identifier of the user to be deleted.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        with self.__db_connection as database:
            user_model = (
                database.session.query(UserModel)
                .filter(UserModel.id == identifier)
                .first()
            )

            if user_model:
                try:
                    database.session.delete(user_model)
                    database.session.commit()
                    return True
                except Exception:
                    database.session.rollback()
                    return False
            return False
