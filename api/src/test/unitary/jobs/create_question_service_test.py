import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.application.services.create_question_service import (
    CreateQuestionService,
)
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.repositories.in_memory_questions_repository import (
    InMemoryQuestionsRepository,
)
from src.test.factories.make_user import MakeUser
from src.test.factories.make_question import MakeQuestion


@pytest.fixture(name="fixture")
def question_service_fixture() -> (
    tuple[CreateQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the CreateQuestionService with an InMemoryQuestionsRepository.

    Returns:
        CreateQuestionService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    questions_repository = InMemoryQuestionsRepository()
    create_question_service = CreateQuestionService(
        users_repository, questions_repository
    )
    return create_question_service, questions_repository, users_repository


def test_created_question_successfully(
    fixture: tuple[
        CreateQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the CreateQuestionService to ensure it creates a question and adds it to the repository.
    """
    create_question_service, questions_repository, users_repository = fixture

    user = MakeUser().make_user()
    users_repository.items.append(user)

    dto = MakeQuestion(user_id=user.get_identifier()).make_question_dto()

    result = create_question_service.execute(dto)

    assert result is None
    assert len(questions_repository.items) == 1
    assert questions_repository.items[0].get_question() == dto.question
    assert questions_repository.items[0].get_question_type() == dto.question_type
    assert questions_repository.items[0].get_user_id() == dto.user_id
    assert questions_repository.items[0].get_company_id() == dto.company_id


def test_error_when_trying_to_create_question_with_user_not_found(
    fixture: tuple[
        CreateQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the CreateQuestionService to ensure it returns an error when trying to create
    a question with a user not found.
    """
    create_question_service, _, users_repository = fixture

    user = MakeUser().make_user()
    users_repository.items.append(user)

    dto = MakeQuestion(user_id=user.get_identifier() + 1).make_question_dto()

    result = create_question_service.execute(dto)

    assert isinstance(result, ResourceNotFoundError)
