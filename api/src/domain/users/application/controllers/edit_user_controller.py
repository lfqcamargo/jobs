from datetime import date
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.edit_user_service import EditUserService
from src.domain.users.application.dto.edit_user_dto import EditUserDTO
from .interfaces.edit_user_controller_interface import EditUserControllerInterface


class EditUserController(EditUserControllerInterface):
    """
    Controller responsible for handling user editing requests.

    This controller coordinates the user editing process. It communicates with the service layer
    to perform the actual update logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when a user does not exist or when an email
    conflict occurs.

    Methods:
        handle(identifier: int, name: str | None, email: str | None, password: str | None,
               birthday_date: date | None, curriculum: bytes | None, country_code: str,
               phone_number: str) -> None:
            Handles the user editing process by calling the service layer with the
            provided user data.
            If any errors occur (e.g., user not found, email conflict, domain errors),
            they are raised
            appropriately.

    Raises:
        ResourceNotFoundError: If the user does not exist in the system.
        AlreadyExistsError: If the new email is already in use by another user.
        DomainError: For any unexpected domain-related errors.
    """

    def __init__(self, service: EditUserService) -> None:
        """
        Initializes the EditUserController with a user service.

        Args:
            service (EditUserService): The service handling user editing logic.
        """
        self.__service = service

    def handle(
        self,
        identifier: int,
        name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        birthday_date: date | None = None,
        curriculum: bytes | None = None,
        country_code: str | None = None,
        phone_number: str | None = None,
    ) -> None:
        dto = EditUserDTO(
            identifier=identifier,
            name=name,
            email=email,
            password=password,
            birthday_date=birthday_date,
            curriculum=curriculum,
            country_code=country_code,
            phone_number=phone_number,
        )

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, ResourceNotFoundError):
                raise result
            if isinstance(result, AlreadyExistsError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
