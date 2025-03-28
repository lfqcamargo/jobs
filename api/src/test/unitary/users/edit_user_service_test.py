import pytest
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.already_exists_error import AlreadyExistsError
from src.domain.users.application.services.edit_user_service import EditUserService
from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.dto.edit_user_dto import EditUserDTO
from src.test.cryptography.fake_password import FakerPassword
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository


@pytest.fixture(name="fixture")
def user_service_fixture() -> tuple[EditUserService, InMemoryUsersRepository]:
    """
    Fixture to initialize the EditUserService with an InMemoryUsersRepository.

    Returns:
        EditUserService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    faker_password = FakerPassword()
    edit_user_service = EditUserService(users_repository, faker_password)
    return edit_user_service, users_repository


def test_editd_user_successfully(
    fixture: tuple[EditUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the EditUserService to ensure it editd user it to the repository.
    """
    edit_user_service, users_repository = fixture

    user = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="hashed_123456789",
    )
    users_repository.items.append(user)

    dto = EditUserDTO(
        name="Camargo Lucas",
        email="lfqcamargo@gmail.com.br",
        birthday_date="11/11/1995",
        identifier=user.get_identifier(),
        password=None,
    )

    result = edit_user_service.execute(dto)

    assert result is None
    assert users_repository.items[0].get_name() == dto.name
    assert users_repository.items[0].get_email() == dto.email
    assert users_repository.items[0].get_birthday_date() == dto.birthday_date
    assert users_repository.items[0].get_password() == "hashed_123456789"

    dto = EditUserDTO(
        name="Camargo Lucas",
        email="lfqcamargo@gmail.com.br",
        birthday_date="11/11/1995",
        identifier=user.get_identifier(),
        password="123456",
    )

    result = edit_user_service.execute(dto)

    assert result is None
    assert users_repository.items[0].get_password() == "hashed_123456"


def test_error_when_trying_to_edit_with_duplicate_email(
    fixture: tuple[EditUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the EditUserService to ensure it returns an error when trying to edit
    a user with a duplicate email.
    """
    edit_user_service, users_repository = fixture

    user_fixed = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=1,
    )
    users_repository.items.append(user_fixed)

    user_test = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com.br",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=2,
    )
    users_repository.items.append(user_test)

    dto = EditUserDTO(
        name="Camargo Lucas",
        email="lfqcamargo@gmail.com",
        birthday_date="11/11/1995",
        identifier=user_test.get_identifier(),
        password=None,
    )

    result = edit_user_service.execute(dto)

    assert isinstance(result, AlreadyExistsError)


def test_error_when_trying_to_edit_with_user_not_exists(
    fixture: tuple[EditUserService, InMemoryUsersRepository],
) -> None:
    """
    Test the EditUserService to ensure it returns an error when trying to edit
    a user with a not exists.
    """
    edit_user_service, users_repository = fixture

    user_fixed = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=1,
    )
    users_repository.items.append(user_fixed)

    user_test = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com.br",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=2,
    )
    users_repository.items.append(user_test)

    dto = EditUserDTO(
        name="Camargo Lucas",
        email="lfqcamargo@gmail.com",
        birthday_date="11/11/1995",
        identifier=user_test.get_identifier() + 1,
        password=None,
    )

    result = edit_user_service.execute(dto)

    assert isinstance(result, ResourNotFoundError)
