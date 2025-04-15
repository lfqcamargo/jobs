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
        curriculum: bytes,
        country_code: str,
        phone_number: str,
        identifier: int = 0,
    ) -> None:
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The user's password.
            birthday_date (date): The birthday date of the user.
            curriculum (bytes, optional): The user's curriculum stored as binary data.
            country_code(str): The country code.
            phone_number(str): Phone number.
            identifier (int, optional): The unique identifier of the user. Defaults to 0.
        """
        super().__init__(identifier)
        self.__name = name
        self.__email = email
        self.__password = password
        self.__birthday_date = birthday_date
        self.__curriculum = curriculum
        self.__country_code = country_code
        self.__phone_number = phone_number

    def get_name(self) -> str:
        """
        Retrieve the user's name.

        Returns:
            str: The name of the user.
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Set the user's name.

        Args:
            name (str): The name to be set for the user.
        """
        self.__name = name

    def get_email(self) -> str:
        """
        Retrieve the user's email.

        Returns:
            str: The email of the user.
        """
        return self.__email

    def set_email(self, email: str) -> None:
        """
        Set the user's email.

        Args:
            email (str): The email to be set for the user.
        """
        self.__email = email

    def get_password(self) -> str:
        """
        Retrieve the user's password.

        Returns:
            str: The password of the user.
        """
        return self.__password

    def set_password(self, password: str) -> None:
        """
        Set the user's password.

        Args:
            password (str): The password to be set for the user.
        """
        self.__password = password

    def get_birthday_date(self) -> date:
        """
        Retrieve the user's birthday date.

        Returns:
            date: The birthday date of the user.
        """
        return self.__birthday_date

    def set_birthday_date(self, birthday_date: date) -> None:
        """
        Set the user's birthday date.

        Args:
            birthday_date (date): The birthday date to be set for the user.
        """
        self.__birthday_date = birthday_date

    def get_curriculum(self) -> bytes | None:
        """
        Retrieve the user's curriculum (binary data).

        Returns:
            bytes | None: The binary data of the user's curriculum, or None if not set.
        """
        return self.__curriculum

    def set_curriculum(self, curriculum: bytes) -> None:
        """
        Set the user's curriculum (binary data).

        Args:
            curriculum (bytes): The binary data to be set for the user's curriculum.
        """
        self.__curriculum = curriculum

    def get_country_code(self) -> str:
        """
        Retrieve the user's country code.

        Returns:
            str: The country_code of the user.
        """
        return self.__country_code

    def set_country_code(self, country_code: str) -> None:
        """
        Set the user's country_code.

        Args:
            country_code (str): The country_code to be set for the user.
        """
        self.__password = country_code

    def get_phone_number(self) -> str:
        """
        Retrieve the user's phone number.

        Returns:
            str: The phone number of the user.
        """
        return self.__phone_number

    def set_phone_number(self, phone_number: str) -> None:
        """
        Set the user's phone_number.

        Args:
            phone_number (str): The phone number to be set for the user.
        """
        self.__password = phone_number

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
            curriculum=props.curriculum,
            country_code=props.country_code,
            phone_number=props.phone_number,
        )

        return user

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
            str: A formatted string containing user details.
        """
        return (
            f"ID: {self.get_identifier()}, name: {self.__name}, email: {self.__email}"
        )
