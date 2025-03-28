import pytest
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.domain.users.application.services.fetch_users_service import FetchUsersService
from src.domain.users.enterprise.entities.user import User
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository


@pytest.fixture(name="fixture")
def user_service_fixture() -> tuple[FetchUsersService, InMemoryUsersRepository]:
    """
    Fixture to initialize the FetchUsersService with an InMemoryUsersRepository.

    Returns:
        FetchUsersService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    fetch_user_service = FetchUsersService(users_repository)
    return fetch_user_service, users_repository


def test_fetched_users_successfully(
    fixture: tuple[FetchUsersService, InMemoryUsersRepository],
) -> None:
    """
    Test the FetchUsersService to ensure it fetched users it to the repository.
    """
    fetch_user_service, users_repository = fixture

    user_1 = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=1,
    )

    user_2 = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=2,
    )

    users_repository.items.append(user_1)
    users_repository.items.append(user_2)

    result = fetch_user_service.execute()

    assert len(result) == 2


def test_error_when_trying_to_fetch_with_users_not_exists(
    fixture: tuple[FetchUsersService, InMemoryUsersRepository],
) -> None:
    """
    Test the FetchUsersService to ensure it returns an error when trying to fetch
    a users with a not exists.
    """
    fetch_user_service, _ = fixture

    result = fetch_user_service.execute()

    assert isinstance(result, ResourNotFoundError)
