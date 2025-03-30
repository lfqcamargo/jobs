import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.delete_skill_service import (
    DeleteSkillService,
)
from src.test.repositories.in_memory_skills_repository import InMemorySkillsRepository
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_skill import MakeSkill


@pytest.fixture(name="fixture")
def skill_service_fixture() -> (
    tuple[DeleteSkillService, InMemorySkillsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the DeleteSkillService with an InMemorySkillsRepository.

    Returns:
        DeleteSkillService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    skills_repository = InMemorySkillsRepository()
    delete_skill_service = DeleteSkillService(skills_repository)
    return delete_skill_service, skills_repository, users_repository


def test_deleted_user_successfully(
    fixture: tuple[
        DeleteSkillService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the DeleteSkillService to ensure it deleted user it to the repository.
    """
    delete_skill_service, skills_repository, _ = fixture

    skill = MakeSkill().make_skill()
    skills_repository.items.append(skill)

    result = delete_skill_service.execute(skill.get_identifier())

    assert result is None
    assert len(skills_repository.items) == 0


def test_error_when_trying_to_delete_with_skill_not_exists(
    fixture: tuple[
        DeleteSkillService, InMemorySkillsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the DeleteSkillService to ensure it returns an error when trying to delete
    a user with a not exists.
    """
    delete_skill_service, skills_repository, _ = fixture

    skill = MakeSkill().make_skill()
    skills_repository.items.append(skill)

    result = delete_skill_service.execute(skill.get_identifier() + 1)

    assert isinstance(result, ResourceNotFoundError)
