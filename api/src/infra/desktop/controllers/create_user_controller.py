from datetime import datetime
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.error_server import ErrorServer
from src.domain.users.application.services.create_user_service import CreateUserService
from src.domain.users.application.dto.create_user_dto import CreateUserDTO
from ..validators.create_user_validator import create_user_validator


class CreateUserController:
    """
    Controller responsible for handling the creation of users.

    Attributes:
        __service (CreateUserService): The service responsible for creating users.
    """

    def __init__(self, service: CreateUserService) -> None:
        """
        Initializes the CreateUserController with a specific CreateUserService.

        Args:
            service (CreateUserService): The service used to create users.
        """
        self.__service = service

    def handle(self, name: str, email: str, birthday_date: str, password: str) -> None:
        """
        Handles the process of creating a user using the provided service.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            birthday_date (str): The birthday date of the user in 'YYYY-MM-DD' format.
            password (str): The password for the user.

        Raises:
            AlreadyExistsError: If the user already exists based on the provided email.
            ValidationError: Validation fields.
            ErrorServer: If an internal server error occurs.
        """

        create_user_validator(name, email, birthday_date, password)
        birthday_date = datetime.strptime(birthday_date, "%d/%m/%Y")
        dto = CreateUserDTO(name, email, password, birthday_date)
        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, AlreadyExistsError):
                raise result

            raise ErrorServer("Erro Interno.")

        return result
