import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.delete_user_service import DeleteUserService
from src.domain.users.enterprise.entities.user import User
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository


@pytest.fixture(name="fixture")
def user_service_fixture() -> tuple[DeleteUserService, InMemoryUsersRepository]:
    """
    Fixture to initialize the DeleteUserService with an InMemoryUsersRepository.

    Returns:
        DeleteUserService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    delete_user_service = DeleteUserService(users_repository)
    return delete_user_service, users_repository


def test_deleted_user_successfully(
    fixture: tuple[DeleteUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the DeleteUserService to ensure it deleted user it to the repository.
    """
    delete_user_service, users_repository = fixture

    user = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
    )
    users_repository.items.append(user)

    result = delete_user_service.execute(user.get_identifier())

    assert result is None
    assert len(users_repository.items) == 0


def test_error_when_trying_to_delete_with_user_not_exists(
    fixture: tuple[DeleteUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the DeleteUserService to ensure it returns an error when trying to delete
    a user with a not exists.
    """
    delete_user_service, users_repository = fixture

    user = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
    )
    users_repository.items.append(user)

    result = delete_user_service.execute(user.get_identifier() + 1)

    assert isinstance(result, ResourceNotFoundError)
