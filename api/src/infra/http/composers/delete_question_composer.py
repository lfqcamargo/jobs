from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.questions_repository import (
    QuestionsRepository,
)
from src.domain.jobs.application.controllers.delete_question_controller import (
    DeleteQuestionController,
)
from src.infra.http.views.delete_question_view import DeleteQuestionView
from src.domain.jobs.application.services.delete_question_service import (
    DeleteQuestionService,
)


def delete_question_composer() -> DeleteQuestionView:
    """
    Composer function to create and return a DeleteQuestionView instance.

    This function initializes the necessary dependencies for question deletion,
    including the QuestionsRepository, DeleteQuestionService, DeleteQuestionController,
    and DeleteQuestionView. It ties all components together to create a complete
    view that can handle question deletion requests.

    Returns:
        DeleteQuestionView: The initialized DeleteQuestionView instance,
        ready to handle HTTP requests.
    """
    questions_repository = QuestionsRepository(db_connection_handler)
    service = DeleteQuestionService(questions_repository)
    controller = DeleteQuestionController(service)
    view = DeleteQuestionView(controller)

    return view
