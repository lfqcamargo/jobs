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
        dto = CreateUserDTO(
            name=raw.name,
            email=raw.email,
            password=raw.password,
            birthday_date=raw.birthday_date,
            curriculum=raw.curriculum,
            identifier=raw.id,
        )
        return User.create(dto)

    @staticmethod
    def to_sql(user: User) -> UserModel:
        """
        Converts a User domain entity to a UserModel instance for database persistence.

        Args:
            user (User): The domain entity representing a user.

        Returns:
            UserModel: A database model instance representing the user.
        """
        return UserModel(
            id=user.get_identifier() if user.get_identifier() != 0 else None,
            name=user.get_name(),
            email=user.get_email(),
            password=user.get_password(),
            birthday_date=user.get_birthday_date(),
            curriculum=user.get_curriculum(),
        )
