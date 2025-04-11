from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.questions_repository import (
    QuestionsRepository,
)
from src.domain.jobs.application.services.edit_question_service import (
    EditQuestionService,
)
from src.domain.jobs.application.controllers.edit_question_controller import (
    EditQuestionController,
)
from src.infra.http.views.edit_question_view import EditQuestionView


def edit_question_composer() -> EditQuestionView:
    """
    Composer function to create and return an EditQuestionView instance.

    This function initializes the necessary dependencies for editing question data,
    including the QuestionsRepository, EditQuestionService, EditQuestionController,
    and EditQuestionView. It ties all components together to create a complete
    view that can handle question editing requests.

    Returns:
        EditQuestionView: The initialized EditQuestionView instance, ready to handle HTTP requests.
    """
    questions_repository = QuestionsRepository(db_connection_handler)
    service = EditQuestionService(questions_repository)
    controller = EditQuestionController(service)
    view = EditQuestionView(controller)

    return view
