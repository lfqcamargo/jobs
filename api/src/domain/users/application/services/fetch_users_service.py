from src.core.errors.resource_not_found_error import ResourNotFoundError
from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ...enterprise.entities.user import User


class FetchUsersService:
    """
    Service responsible for fetching all users.

    This class handles the business logic for retrieving users from the repository.
    If no users are found, an error is raised. It ensures that the data is consistent
    and properly fetched from the underlying data source.
    """

    def __init__(
        self,
        users_repository: UsersRepositoryInterface,
    ) -> list[User] | ResourNotFoundError:
        """
        Initializes the FetchUsersService with a user repository.

        This service class requires a repository that implements the UsersRepositoryInterface
        to fetch the list of users from the data source.

        Args:
            users_repository (UsersRepositoryInterface): The repository responsible for
            fetching user data.

        Returns:
            None
        """
        self.__users_repository = users_repository

    def execute(self) -> None:
        """
        Executes the process of fetching users from the repository.

        It retrieves the list of all users and raises an error if no users are found.

        Args:
            None

        Returns:
            list[User]: A list of User objects representing all users in the repository.

        Raises:
            ResourNotFoundError: If no users are found in the repository.
        """
        users = self.__users_repository.fetch_all()
        if len(users) == 0:
            return ResourNotFoundError(message="Users not found.", resource="users")

        return users
