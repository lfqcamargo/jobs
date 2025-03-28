from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.interfaces.users_repository_interface import (
    UsersRepositoryInterface,
)


class InMemoryUsersRepository(UsersRepositoryInterface):
    """
    In-memory implementation of the UserRepository for testing purposes.

    This class provides an in-memory storage mechanism for user entities,
    useful for unit testing without relying on a database.
    """

    def __init__(self) -> None:
        self.items: list[User] = []

    def create(self, user: User) -> None:
        self.items.append(user)

    def find_by_email(self, email: str) -> User | None:
        return next((user for user in self.items if user.get_email() == email), None)

    def find_by_identifier(self, identifier: int) -> User | None:
        return next(
            (user for user in self.items if user.get_identifier() == identifier), None
        )

    def fetch_all(self) -> list[User] | None:
        return self.items if self.items else None

    def save(self, user: User) -> bool:
        for i, existing_user in enumerate(self.items):
            if existing_user.get_identifier() == user.get_identifier():
                self.items[i] = user
                return True
        return False

    def delete(self, identifier: int) -> bool:
        for i, user in enumerate(self.items):
            if user.get_identifier() == identifier:
                del self.items[i]
                return True
        return False
