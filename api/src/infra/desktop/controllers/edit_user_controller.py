from datetime import datetime
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.error_server import ErrorServer
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.domain.users.application.services.edit_user_service import EditUserService
from src.domain.users.application.dto.edit_user_dto import EditUserDTO
from ..validators.edit_user_validator import edit_user_validator


class EditUserController:
    """
    Controller responsible for handling user editing requests.

    Attributes:
        __service (EditUserService): The service responsible for editing users.
    """

    def __init__(self, service: EditUserService) -> None:
        """
        Initializes the EditUserController with a specific EditUserService.

        Args:
            service (EditUserService): The service used to edit user details.
        """
        self.__service = service

    def handle(
        self,
        identifier: int,
        name: str,
        email: str,
        birthday_date: str,
        password: str | None,
    ) -> None:
        """
        Handles the process of editing an existing user's details using the provided service.

        This method validates the input fields, converts the `birthday_date` to a `datetime` object,
        and passes the data transfer object (DTO) to the service for processing.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            birthday_date (str): The birthday date of the user in 'YYYY-MM-DD' format.
            password (str | None): The password of the user, which can be omitted if not changing.

        Raises:
            ResourNotFoundError: If no user is found with the provided identifier.
            ValidationError: If any of the fields fail validation.
            ErrorServer: If an internal server error occurs.
        """

        edit_user_validator(identifier, name, email, birthday_date, password)

        birthday_date = datetime.strptime(birthday_date, "%d/%m/%Y")

        dto = EditUserDTO(name, email, password, birthday_date, identifier)

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, AlreadyExistsError):
                raise result
            if isinstance(result, ResourNotFoundError):
                raise result

            raise ErrorServer("Erro Interno.")

        return result
