from src.infra.database.postgres.repositories.questions_repository import (
    QuestionsRepository,
)
from src.domain.jobs.application.services.fetch_questions_service import (
    FetchQuestionsService,
)
from src.domain.jobs.application.controllers.fetch_questions_controller import (
    FetchQuestionsController,
)
from src.infra.http.views.fetch_questions_view import FetchQuestionsView
from src.infra.database.postgres.settings.connection import db_connection_handler


def fetch_questions_composer() -> FetchQuestionsView:
    """
    Composer function to create and return a FetchQuestionsView instance.

    This function initializes the necessary dependencies for fetching questions,
    including the QuestionsRepository, FetchQuestionsService, FetchQuestionsController,
    and FetchQuestionsView. It ties all components together to create a complete
    view that can handle question fetching requests.

    Returns:
        FetchQuestionsView: The initialized FetchQuestionsView instance, ready to
        handle HTTP requests.
    """
    questions_repository = QuestionsRepository(db_connection_handler)
    service = FetchQuestionsService(questions_repository)
    controller = FetchQuestionsController(service)
    view = FetchQuestionsView(controller)

    return view
