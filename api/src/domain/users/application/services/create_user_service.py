from ..interfaces.users_repository_interface import UsersRepositoryInterface
from ..dto.create_user_dto import CreateUserDTO
from ...enterprise.entities.user import User


class CreateUserService:
    """
    Service responsible for user creation logic.

    This class handles the business logic for creating a new user,
    ensuring that a user with the given email does not already exist.
    """

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        """
        Initializes the CreateUserService with a user repository.

        Args:
            users_repository (UsersRepositoryInterface): The repository responsible for user data operations.
        """
        self.__users_repository = users_repository

    def execute(self, props: CreateUserDTO) -> None:
        """
        Executes the user creation process.

        Checks if the email already exists; if not, creates a new user.

        Args:
            props (CreateUserDTO): The data transfer object containing user details.

        Returns:
            None
        """
        user_email = self.__users_repository.find_by_email(props.email)

        if user_email is not None:
            return

        user = User.create(props)
        return self.__users_repository.create(user)
