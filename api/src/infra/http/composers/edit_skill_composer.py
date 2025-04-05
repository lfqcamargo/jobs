from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.skills_repository import SkillsRepository
from src.domain.users.application.services.edit_skill_service import EditSkillService
from src.domain.users.application.controllers.edit_skill_controller import (
    EditSkillController,
)
from src.infra.http.views.edit_skill_view import EditSkillView


def edit_skill_composer() -> EditSkillView:
    """
    Composer function to create and return an EditSkillView instance.

    This function initializes the necessary dependencies for editing skill data,
    including the SkillsRepository, EditSkillService, EditSkillController,
    and EditSkillView. It ties all components together to create a complete
    view that can handle skill editing requests.

    Returns:
        EditSkillView: The initialized EditSkillView instance, ready to handle HTTP requests.
    """
    skills_repository = SkillsRepository(db_connection_handler)
    service = EditSkillService(skills_repository)
    controller = EditSkillController(service)
    view = EditSkillView(controller)

    return view
