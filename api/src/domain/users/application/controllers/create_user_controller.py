from datetime import date
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.services.create_user_service import CreateUserService
from src.domain.users.application.dto.create_user_dto import CreateUserDTO
from .interfaces.create_user_controller_interface import CreateUserControllerInterface


class CreateUserController(CreateUserControllerInterface):
    """
    Controller responsible for handling user creation requests.

    This controller coordinates the user creation process. It communicates with the service layer
    to perform the actual creation logic. Additionally, it raises relevant exceptions if errors
    are encountered during the process, such as when a user already exists or when domain-related
    errors occur.

    Methods:
        handle(name: str, email: str, password: str, birthday_date: date,
        curriculum: bytes) -> None:
            Handles the user creation process by calling the service layer with the
            provided user data.
            If any errors occur (e.g., user already exists, domain errors), they are raised
            appropriately.

    Raises:
        AlreadyExistsError: If the user already exists in the system.
        DomainError: For any unexpected domain-related errors.
    """

    def __init__(self, service: CreateUserService) -> None:
        """
        Initializes the CreateUserController with a user service.

        Args:
            service (CreateUserService): The service handling user creation logic.
        """
        self.__service = service

    def handle(
        self,
        name: str,
        email: str,
        password: str,
        birthday_date: date,
        curriculum: bytes,
    ) -> None:
        dto = CreateUserDTO(
            name=name,
            email=email,
            password=password,
            birthday_date=birthday_date,
            curriculum=curriculum,
        )

        result = self.__service.execute(dto)

        if isinstance(result, Exception):
            if isinstance(result, AlreadyExistsError):
                raise result
            if isinstance(result, DomainError):
                raise result

            raise DomainError("An unexpected domain error occurred.")

        return None
