from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from ..interfaces.users_repository_interface import UsersRepositoryInterface


class DeleteUserService:
    """
    Service responsible for deleting a user.

    This class handles the business logic for deleting a user by its identifier,
    ensuring that the user exists before attempting to delete.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
    ) -> None:
        """
        Initializes the DeleteUserService with a user repository.

        Args:
            users_repository (UsersRepositoryInterface): The repository responsible for
            user data operations (find, delete, etc.).
        """
        self.__users_repository = users_repository

    def execute(self, identifier: int) -> None | ResourceNotFoundError:
        """
        Executes the user deletion process.

        This method checks if the user with the given identifier exists. If the user is found,
        it proceeds to delete the user. If the user is not found, a `ResourceNotFoundError` is raised.

        Args:
            identifier (int): The identifier of the user to be deleted.

        Raises:
            ResourceNotFoundError: If the user is not found with the given identifier.
            DomainError: If an error occurs during the deletion process.

        Returns:
            None | ResourceNotFoundError
        """
        user = self.__users_repository.find_by_identifier(identifier)

        if user is None:
            return ResourceNotFoundError(
                message="Usuário não encontrado.", resource="Usuário"
            )

        result = self.__users_repository.delete(user.get_identifier())

        if result is False:
            return DomainError(message="Erro ao tentar atualizar banco de dados.")

        return None
