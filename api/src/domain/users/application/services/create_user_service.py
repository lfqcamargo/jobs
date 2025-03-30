from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)
from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ..dto.create_user_dto import CreateUserDTO
from ...enterprise.entities.user import User


class CreateUserService:
    """
    Service responsible for user creation logic.

    This class handles the business logic for creating a new user,
    ensuring that a user with the given email does not already exist.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
        password_handler: PasswordHandlerInterface,
    ) -> None:
        """
        Initializes the CreateUserService with a user repository.

        Args:
            users_repository (UsersRepositoryInterface): The repository responsible for
            user data operations.
            password_handler (PasswordHandlerInterface): Driver to manage user password.
        """
        self.__users_repository = users_repository
        self.__password_handler = password_handler

    def execute(self, props: CreateUserDTO) -> None | AlreadyExistsError | DomainError:
        """
        Executes the user creation process.

        Checks if the email already exists; if not, creates a new user.

        Args:
            props (CreateUserDTO): The data transfer object containing user details.

        Returns:
            None | AlreadyExistsError | DomainError
        """
        user_email = self.__users_repository.find_by_email(props.email)

        if user_email is not None:
            return AlreadyExistsError(message="Email já cadastrado.", field="email")

        props.password = self.__password_handler.encrypt_password(props.password)

        user = User.create(props)
        print(user.get_curriculum())
        result = self.__users_repository.create(user)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
