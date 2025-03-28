import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.fetch_skills_service import (
    FetchSkillsService,
)
from src.domain.users.enterprise.entities.skill import Skill
from src.domain.users.enterprise.enums.skill_level import SkillLevel
from src.test.repositories.in_memory_skills_repository import InMemorySkillsRepository
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository


@pytest.fixture(name="fixture")
def skill_service_fixture() -> (
    tuple[FetchSkillsService, InMemorySkillsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the FetchSkillService with an InMemorySkillsRepository.

    Returns:
        FetchSkillService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    skills_repository = InMemorySkillsRepository()
    fetch_skill_service = FetchSkillsService(skills_repository)
    return fetch_skill_service, skills_repository, users_repository


def test_fetched_skills_successfully(
    fixture: tuple[
        FetchSkillsService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the FetchSkillService to ensure it fetched skills it to the repository.
    """
    fetch_skill_service, skills_repository, _ = fixture

    skill_1 = Skill(
        description="python",
        time_month=12,
        level=SkillLevel.MID_LEVEL,
        user_id=1,
        identifier=1,
    )
    skills_repository.items.append(skill_1)

    skill_2 = Skill(
        description="javascript",
        time_month=24,
        level=SkillLevel.SENIOR,
        user_id=1,
        identifier=2,
    )
    skills_repository.items.append(skill_2)

    skill_3 = Skill(
        description="javascript",
        time_month=24,
        level=SkillLevel.SENIOR,
        user_id=2,
        identifier=2,
    )
    skills_repository.items.append(skill_3)

    result = fetch_skill_service.execute(skill_1.get_user_id())

    assert len(result) == 2


def test_error_when_trying_to_fetch_with_skill_not_exists(
    fixture: tuple[
        FetchSkillsService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the FetchSkillsService to ensure it returns an error when trying to fetch
    a user with a not exists.
    """
    fetch_skill_service, skills_repository, _ = fixture

    skill = Skill(
        description="python",
        time_month=12,
        level=SkillLevel.MID_LEVEL,
        user_id=1,
        identifier=1,
    )
    skills_repository.items.append(skill)

    result = fetch_skill_service.execute(skill.get_user_id() + 1)

    assert isinstance(result, ResourceNotFoundError)
