import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.create_skill_service import (
    CreateSkillService,
)
from src.domain.users.application.dto.create_skill_dto import CreateSkillDTO
from src.domain.users.enterprise.entities.user import User
from src.domain.users.enterprise.enums.skill_level import SkillLevel
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.repositories.in_memory_skills_repository import InMemorySkillsRepository


@pytest.fixture(name="fixture")
def skill_service_fixture() -> (
    tuple[CreateSkillService, InMemorySkillsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the CreateSkillService with an InMemorySkillsRepository.

    Returns:
        CreateSkillService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    skills_repository = InMemorySkillsRepository()
    create_skill_service = CreateSkillService(users_repository, skills_repository)
    return create_skill_service, skills_repository, users_repository


def test_created_skill_successfully(
    fixture: tuple[
        CreateSkillService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the CreateSkillService to ensure it creates a skill and adds it to the repository.
    """
    create_skill_service, skills_repository, users_repository = fixture

    user = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=1,
    )
    users_repository.items.append(user)

    dto = CreateSkillDTO(
        description="python",
        time_month=12,
        level=SkillLevel.MID_LEVEL,
        user_id=user.get_identifier(),
    )

    result = create_skill_service.execute(dto)

    assert result is None
    assert len(skills_repository.items) == 1
    assert skills_repository.items[0].get_description() == dto.description
    assert skills_repository.items[0].get_time_month() == dto.time_month
    assert skills_repository.items[0].get_level() == dto.level
    assert skills_repository.items[0].get_user_id() == dto.user_id


def test_error_when_trying_to_create_with_user_not_found(
    fixture: tuple[
        CreateSkillService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the CreateSkillService to ensure it returns an error when trying to create
    a skill with a user not found.
    """
    create_skill_service, _, users_repository = fixture

    user = User(
        name="Lucas Camargo",
        email="lfqcamargo@gmail.com",
        birthday_date="22/11/1995",
        password="123456789",
        identifier=1,
    )
    users_repository.items.append(user)

    dto = CreateSkillDTO(
        description="python",
        time_month=12,
        level=SkillLevel.MID_LEVEL,
        user_id=user.get_identifier() + 1,
    )

    create_skill_service.execute(dto)
    result = create_skill_service.execute(dto)

    assert isinstance(result, ResourceNotFoundError)
