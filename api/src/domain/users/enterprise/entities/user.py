from datetime import date
from src.core.entities.entity import Entity
from src.domain.users.application.dto.create_user_dto import CreateUserDTO


class User(Entity):
    """
    Represents a user entity.

    This class extends the base Entity class and includes specific attributes
    and methods related to a user.
    """

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        birthday_date: date,
        identifier: int = 0,
    ) -> None:
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The user's password.
            birthday_date (date): The birthday date of the user.
            identifier (int, optional): The unique identifier of the user. Defaults to 0.
        """
        super().__init__(identifier)
        self.__name = name
        self.__email = email
        self.__password = password
        self.__birthday_date = birthday_date

    def get_name(self) -> str:
        """
        Retrieve the user's name.

        Returns:
            str: The name of the user.
        """
        return self.__name

    def get_email(self) -> str:
        """
        Retrieve the user's email.

        Returns:
            str: The email of the user.
        """
        return self.__email

    def get_password(self) -> str:
        """
        Retrieve the user's password.

        Returns:
            str: The password of the user.
        """
        return self.__password

    def get_birthday_date(self) -> date:
        """
        Retrieve the user's birthday date.

        Returns:
            date: The birthday date of the user.
        """
        return self.__birthday_date

    @staticmethod
    def create(props: CreateUserDTO) -> "User":
        """
        Factory method to create a new User instance from a DTO.

        Args:
            props (CreateUserDTO): Data Transfer Object containing user details.

        Returns:
            User: A new instance of User with the given properties.
        """
        user: User = User(
            name=props.name,
            email=props.email,
            password=props.password,
            birthday_date=props.birthday_date,
            identifier=props.identifier,
        )

        return user

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
            str: A formatted string containing user details.
        """
        return f"ID: {self.__identifier}, name: {self.__name}, email: {self.__email}"
