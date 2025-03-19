from src.domain.users.application.services.create_user_service import CreateUserService
from src.domain.users.application.dto.create_user_dto import CreateUserDTO


class CreateUserController:
    """
    Controller responsible for handling user creation requests.
    """

    def __init__(self, service: CreateUserService) -> None:
        """
        Initializes the CreateUserController with a user service.

        Args:
            service (CreateUserService): The service handling user creation logic.
        """
        self.__service = service

    def handle(self, props: CreateUserDTO) -> None:
        """
        Handles the request to create a new user.

        Args:
            props (CreateUserDTO): The data transfer object containing user details.

        Returns:
            None
        """
        return self.__service.execute(props)
