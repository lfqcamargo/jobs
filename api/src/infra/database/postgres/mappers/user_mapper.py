from src.infra.database.postgres.models.user_model import UserModel
from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.dto.create_user_dto import CreateUserDTO


class UserMapper:
    """
    Mapper class for converting between UserModel (database model) and User (domain entity).
    """

    @staticmethod
    def to_domain(raw: UserModel) -> User:
        """
        Converts a UserModel instance to a User domain entity.

        Args:
            raw (UserModel): The database model instance representing a user.

        Returns:
            User: A domain entity representing the user.
        """
        print(raw)
        dto = CreateUserDTO(
            name=raw.name,
            email=raw.email,
            password=raw.password,
            birthday_date=raw.birthday_date,
            identifier=raw.id,
        )
        return User.create(dto)
