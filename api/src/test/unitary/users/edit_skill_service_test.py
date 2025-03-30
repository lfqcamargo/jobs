import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.application.services.edit_skill_service import (
    EditSkillService,
)
from src.test.repositories.in_memory_skills_repository import InMemorySkillsRepository
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_skill import MakeSkill


@pytest.fixture(name="fixture")
def skill_service_fixture() -> (
    tuple[EditSkillService, InMemorySkillsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the EditSkillService with an InMemorySkillsRepository.

    Returns:
        EditSkillService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    skills_repository = InMemorySkillsRepository()
    edit_skill_service = EditSkillService(skills_repository)
    return edit_skill_service, skills_repository, users_repository


def test_edited_user_successfully(
    fixture: tuple[EditSkillService, InMemorySkillsRepository, InMemoryUsersRepository],
) -> None:
    """
    Test the EditSkillService to ensure it edited user it to the repository.
    """
    edit_skill_service, skills_repository, _ = fixture

    skill = MakeSkill().make_skill()
    skills_repository.items.append(skill)

    dto = MakeSkill(
        user_id=skill.get_user_id(), identifier=skill.get_identifier()
    ).make_skill_dto()

    result = edit_skill_service.execute(dto)

    assert result is None
    assert skills_repository.items[0].get_description() == dto.description
    assert skills_repository.items[0].get_time_month() == dto.time_month
    assert skills_repository.items[0].get_level() == dto.level
    assert skills_repository.items[0].get_user_id() == dto.user_id
    assert skills_repository.items[0].get_identifier() == dto.identifier


def test_error_when_trying_to_edit_with_skill_not_exists(
    fixture: tuple[EditSkillService, InMemorySkillsRepository, InMemoryUsersRepository],
) -> None:
    """
    Test the EditSkillService to ensure it returns an error when trying to edit
    a user with a not exists.
    """
    edit_skill_service, skills_repository, _ = fixture

    skill = MakeSkill().make_skill()
    skills_repository.items.append(skill)

    dto = MakeSkill(identifier=skill.get_identifier() + 1).make_skill_dto()

    result = edit_skill_service.execute(dto)

    assert isinstance(result, ResourceNotFoundError)
