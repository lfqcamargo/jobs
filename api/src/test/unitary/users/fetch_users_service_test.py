import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.fetch_users_service import FetchUsersService
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_user import MakeUser


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

    user_1 = MakeUser().make_user()
    user_2 = MakeUser().make_user()

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

    assert isinstance(result, ResourceNotFoundError)
