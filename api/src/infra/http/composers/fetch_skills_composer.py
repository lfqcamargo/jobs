from src.infra.database.postgres.repositories.skills_repository import SkillsRepository
from src.domain.users.application.services.fetch_skills_service import (
    FetchSkillsService,
)
from src.domain.users.application.controllers.fetch_skills_controller import (
    FetchSkillsController,
)
from src.infra.http.views.fetch_skills_view import FetchSkillsView
from src.infra.database.postgres.settings.connection import db_connection_handler


def fetch_skills_composer() -> FetchSkillsView:
    """
    Composer function to create and return a FetchSkillsView instance.

    This function initializes the necessary dependencies for fetching skills,
    including the SkillsRepository, FetchSkillsService, FetchSkillsController,
    and FetchSkillsView. It ties all components together to create a complete
    view that can handle skill fetching requests.

    Returns:
        FetchSkillsView: The initialized FetchSkillsView instance, ready to handle HTTP requests.
    """
    skills_repository = SkillsRepository(db_connection_handler)
    service = FetchSkillsService(skills_repository)
    controller = FetchSkillsController(service)
    view = FetchSkillsView(controller)

    return view
