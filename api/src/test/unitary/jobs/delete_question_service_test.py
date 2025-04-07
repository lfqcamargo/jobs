import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.application.services.delete_question_service import (
    DeleteQuestionService,
)
from src.test.repositories.in_memory_questions_repository import (
    InMemoryQuestionsRepository,
)
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_question import MakeQuestion


@pytest.fixture(name="fixture")
def question_service_fixture() -> (
    tuple[DeleteQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the DeleteQuestionService with an InMemoryQuestionsRepository.

    Returns:
        DeleteQuestionService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    questions_repository = InMemoryQuestionsRepository()
    delete_question_service = DeleteQuestionService(questions_repository)
    return delete_question_service, questions_repository, users_repository


def test_deleted_question_successfully(
    fixture: tuple[
        DeleteQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the DeleteQuestionService to ensure it deletes a question from the repository.
    """
    delete_question_service, questions_repository, _ = fixture

    question = MakeQuestion().make_question()
    questions_repository.items.append(question)

    result = delete_question_service.execute(question.get_identifier())

    assert result is None
    assert len(questions_repository.items) == 0


def test_error_when_trying_to_delete_with_question_not_exists(
    fixture: tuple[
        DeleteQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the DeleteQuestionService to ensure it returns an error when trying to delete
    a question that does not exist.
    """
    delete_question_service, questions_repository, _ = fixture

    question = MakeQuestion().make_question()
    questions_repository.items.append(question)

    result = delete_question_service.execute(question.get_identifier() + 1)

    assert isinstance(result, ResourceNotFoundError)
