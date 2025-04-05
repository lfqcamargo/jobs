from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.skills_repository import SkillsRepository
from src.domain.users.application.controllers.delete_skill_controller import (
    DeleteSkillController,
)
from src.infra.http.views.delete_skill_view import DeleteSkillView
from src.domain.users.application.services.delete_skill_service import (
    DeleteSkillService,
)


def delete_skill_composer() -> DeleteSkillView:
    """
    Composer function to create and return a DeleteSkillView instance.

    This function initializes the necessary dependencies for skill deletion,
    including the SkillsRepository, DeleteSkillService, DeleteSkillController,
    and DeleteSkillView. It ties all components together to create a complete
    view that can handle skill deletion requests.

    Returns:
        DeleteSkillView: The initialized DeleteSkillView instance, ready to handle HTTP requests.
    """
    skills_repository = SkillsRepository(db_connection_handler)
    service = DeleteSkillService(skills_repository)
    controller = DeleteSkillController(service)
    view = DeleteSkillView(controller)

    return view
