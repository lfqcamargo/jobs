from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.error_server import ErrorServer
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

    def execute(self, identifier: int) -> None | ResourNotFoundError:
        """
        Executes the user deletion process.

        This method checks if the user with the given identifier exists. If the user is found,
        it proceeds to delete the user. If the user is not found, a `ResourNotFoundError` is raised.

        Args:
            identifier (int): The identifier of the user to be deleted.

        Raises:
            ResourNotFoundError: If the user is not found with the given identifier.
            ErrorServer: If an error occurs during the deletion process.

        Returns:
            None | ResourNotFoundError
        """
        user = self.__users_repository.find_by_identifier(identifier)

        if user is None:
            return ResourNotFoundError(
                message="Usuário não encontrado.", resource="Usuário"
            )

        result = self.__users_repository.delete(user.get_identifier())

        if result is False:
            return ErrorServer(message="Erro ao tentar atualizar banco de dados.")

        return None
