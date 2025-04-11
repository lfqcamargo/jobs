from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.questions_repository import (
    QuestionsRepository,
)
from src.domain.jobs.application.services.create_question_service import (
    CreateQuestionService,
)
from src.domain.jobs.application.controllers.create_question_controller import (
    CreateQuestionController,
)
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.infra.http.views.create_question_view import CreateQuestionView


def create_question_composer() -> CreateQuestionView:
    """
    Composer function to create and return a CreateQuestionView instance.

    This function initializes the necessary dependencies for question creation,
    including the UsersRepository, QuestionsRepository, CreateQuestionService,
    CreateQuestionController,
    and CreateQuestionView. It ties all components together to create a complete
    view that can handle question creation requests.

    Returns:
        CreateQuestionView: The initialized CreateQuestionView instance,
        ready to handle HTTP requests.
    """
    users_repository = UsersRepository(db_connection_handler)
    questions_repository = QuestionsRepository(db_connection_handler)
    service = CreateQuestionService(users_repository, questions_repository)
    controller = CreateQuestionController(service)
    view = CreateQuestionView(controller)

    return view
