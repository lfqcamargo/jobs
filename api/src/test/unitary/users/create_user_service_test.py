import pytest
from src.core.errors.already_exists_error import AlreadyExistsError
from src.domain.users.application.services.create_user_service import CreateUserService
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.cryptography.fake_password import FakerPassword
from src.domain.users.application.dto.create_user_dto import CreateUserDTO


@pytest.fixture(name="fixture")
def user_service_fixture() -> tuple[CreateUserService, InMemoryUsersRepository]:
    """
    Fixture to initialize the CreateUserService with an InMemoryUsersRepository.

    Returns:
        CreateUserService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    faker_password = FakerPassword()
    create_user_service = CreateUserService(users_repository, faker_password)
    return create_user_service, users_repository


def test_created_user_successfully(
    fixture: tuple[CreateUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = fixture

    dto = CreateUserDTO(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
    )

    result = create_user_service.execute(dto)

    assert result is None
    assert len(users_repository.items) == 1
    assert users_repository.items[0].get_email() == dto.email
    assert users_repository.items[0].get_password() == "hashed_123456789"


def test_error_when_trying_to_create_with_duplicate_email(
    fixture: tuple[CreateUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the CreateUserService to ensure it returns an error when trying to create
    a user with a duplicate email.
    """
    create_user_service, _ = fixture

    dto = CreateUserDTO(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
    )

    create_user_service.execute(dto)
    result = create_user_service.execute(dto)

    assert isinstance(result, AlreadyExistsError)
