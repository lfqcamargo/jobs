import pytest
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.jobs.application.services.edit_question_service import (
    EditQuestionService,
)
from src.test.repositories.in_memory_questions_repository import (
    InMemoryQuestionsRepository,
)
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_question import MakeQuestion


@pytest.fixture(name="fixture")
def question_service_fixture() -> (
    tuple[EditQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository]
):
    """
    Fixture to initialize the EditQuestionService with an InMemoryQuestionsRepository.

    Returns:
        EditQuestionService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    questions_repository = InMemoryQuestionsRepository()
    edit_question_service = EditQuestionService(questions_repository)
    return edit_question_service, questions_repository, users_repository


def test_edited_question_successfully(
    fixture: tuple[
        EditQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the EditQuestionService to ensure it edits a question in the repository.
    """
    edit_question_service, questions_repository, _ = fixture

    question = MakeQuestion().make_question()
    questions_repository.items.append(question)

    dto = MakeQuestion(
        user_id=question.get_user_id(),
        company_id=question.get_company_id(),
        identifier=question.get_identifier(),
    ).make_question_dto()

    result = edit_question_service.execute(dto)

    assert result is None
    assert questions_repository.items[0].get_question() == dto.question
    assert questions_repository.items[0].get_response() == dto.response
    assert questions_repository.items[0].get_date_time() == dto.date_time
    assert questions_repository.items[0].get_question_type() == dto.question_type
    assert questions_repository.items[0].get_user_id() == dto.user_id
    assert questions_repository.items[0].get_company_id() == dto.company_id
    assert questions_repository.items[0].get_identifier() == dto.identifier


def test_error_when_trying_to_edit_with_question_not_exists(
    fixture: tuple[
        EditQuestionService, InMemoryQuestionsRepository, InMemoryUsersRepository
    ],
) -> None:
    """
    Test the EditQuestionService to ensure it returns an error when trying to edit
    a question that does not exist.
    """
    edit_question_service, questions_repository, _ = fixture

    question = MakeQuestion().make_question()
    questions_repository.items.append(question)

    dto = MakeQuestion(identifier=question.get_identifier() + 1).make_question_dto()

    result = edit_question_service.execute(dto)

    assert isinstance(result, ResourceNotFoundError)
