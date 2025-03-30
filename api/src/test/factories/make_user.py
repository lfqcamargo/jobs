from datetime import date
from faker import Faker
from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.dto.create_user_dto import CreateUserDTO
from src.test.cryptography.fake_password import FakerPassword

faker = Faker()


class MakeUser:
    """
    Creates a User object with default values, allowing overrides for specific attributes.

    Args:
        identifier (Optional[int]): User's unique identifier.
        name (Optional[str]): User's name.
        email (Optional[str]): User's email.
        password (Optional[str]): User's password.
        birthday_date (Optional[str]): User's birthday date.
        curriculum (Optional[bytes]): User's curriculum in bytes.

    Returns:
        User: The created User instance with the provided or default properties.
    """

    def __init__(
        self,
        identifier: int = None,
        name: str = None,
        email: str = None,
        password: str = None,
        birthday_date: date = None,
        curriculum: bytes = None,
    ) -> None:
        self.identifier = identifier or faker.random_int(min=1, max=100)
        self.name = name or faker.name()
        self.email = email or faker.email()
        self.password = password or faker.password()
        self.birthday_date = birthday_date or faker.date_of_birth()
        self.curriculum = curriculum or faker.binary(length=1024)

    def make_user_dto(self) -> CreateUserDTO:
        """Creates a CreateUserDTO with generated or provided data."""
        return CreateUserDTO(
            identifier=self.identifier,
            name=self.name,
            email=self.email,
            password=self.password,
            birthday_date=self.birthday_date,
            curriculum=self.curriculum,
        )

    def make_user(self) -> User:
        """Creates a User entity from a DTO."""
        self.password = FakerPassword().encrypt_password(self.password)
        return User.create(self.make_user_dto())
