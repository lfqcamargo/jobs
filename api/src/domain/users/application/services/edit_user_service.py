from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)
from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ..dto.edit_user_dto import EditUserDTO


class EditUserService:
    """
    Service responsible for editing user data.

    This class handles the business logic for updating an existing user's data,
    ensuring that the provided email does not conflict with another user's email.

    Attributes:
        __users_repository (UsersRepositoryInterface): Repository for user data operations.
        __password_handler (PasswordHandlerInterface): Handler for encrypting and managing
        user passwords.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
        password_handler: PasswordHandlerInterface,
    ) -> None:
        """
        Initializes the EditUserService with a user repository and password handler.

        Args:
            users_repository (UsersRepositoryInterface): The repository responsible for user
            data operations.
            password_handler (PasswordHandlerInterface): The handler responsible for encrypting
            user passwords.
        """
        self.__users_repository = users_repository
        self.__password_handler = password_handler

    def execute(
        self, props: EditUserDTO
    ) -> None | AlreadyExistsError | ResourceNotFoundError:
        """
        Executes the user data editing process.

        This method verifies if the user exists, checks for any email conflicts,
        and updates the user's details. It also updates the password if provided.

        Args:
            props (EditUserDTO): The data transfer object containing the user details to be updated.

        Returns:
            None | ResourceNotFoundError | AlreadyExistsError
        """
        user = self.__users_repository.find_by_identifier(props.identifier)

        if user is None:
            return ResourceNotFoundError("Usuário não encontrado.", resource="Usuário")

        if user.get_email() != props.email:
            user_email = self.__users_repository.find_by_email(props.email)

            if user_email is not None:
                return AlreadyExistsError(message="Email já cadastrado.", field="email")

        if props.password is not None:
            user.set_password(self.__password_handler.encrypt_password(props.password))

        user.set_email(props.email)
        user.set_name(props.name)
        user.set_birthday_date(props.birthday_date)

        result = self.__users_repository.save(user)

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
