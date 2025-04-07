import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.application.services.fetch_questions_service import (
    FetchQuestionsService,
)
from src.test.repositories.in_memory_questions_repository import (
    InMemoryQuestionsRepository,
)
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_question import MakeQuestion


@pytest.fixture(name="fixture")
def question_service_fixture() -> (
    tuple[FetchQuestionsService, InMemoryQuestionsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the FetchQuestionsService with an InMemoryQuestionsRepository.

    Returns:
        FetchQuestionsService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    questions_repository = InMemoryQuestionsRepository()
    fetch_question_service = FetchQuestionsService(questions_repository)
    return fetch_question_service, questions_repository, users_repository


def test_fetched_questions_successfully(
    fixture: tuple[
        FetchQuestionsService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the FetchQuestionsService to ensure it fetched questions from the repository.
    """
    fetch_question_service, questions_repository, _ = fixture

    question_1 = MakeQuestion(user_id=1).make_question()
    questions_repository.items.append(question_1)

    question_2 = MakeQuestion(user_id=1).make_question()
    questions_repository.items.append(question_2)

    question_3 = MakeQuestion(user_id=2).make_question()
    questions_repository.items.append(question_3)

    result = fetch_question_service.execute(question_1.get_user_id())

    assert len(result) == 2


def test_error_when_trying_to_fetch_with_question_not_exists(
    fixture: tuple[
        FetchQuestionsService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the FetchQuestionsService to ensure it returns an error when trying to fetch
    questions for a user that does not exist.
    """
    fetch_question_service, questions_repository, _ = fixture

    question = MakeQuestion().make_question()
    questions_repository.items.append(question)

    result = fetch_question_service.execute(question.get_user_id() + 1)

    assert isinstance(result, ResourceNotFoundError)
