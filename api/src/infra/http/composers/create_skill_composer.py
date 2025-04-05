from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.skills_repository import SkillsRepository
from src.domain.users.application.services.create_skill_service import (
    CreateSkillService,
)
from src.domain.users.application.controllers.create_skill_controller import (
    CreateSkillController,
)
from src.infra.database.postgres.repositories.users_repository import (
    UsersRepository,
)
from src.infra.http.views.create_skill_view import CreateSkillView


def create_skill_composer() -> CreateSkillView:
    """
    Composer function to create and return a CreateSkillView instance.

    This function initializes the necessary dependencies for skill creation,
    including the UserssRepository, SkillsRepository, CreateSkillService, CreateSkillController,
    and CreateSkillView. It ties all components together to create a complete
    view that can handle skill creation requests.

    Returns:
        CreateSkillView: The initialized CreateSkillView instance, ready to handle HTTP requests.
    """
    users_repository = UsersRepository(db_connection_handler)
    skills_repository = SkillsRepository(db_connection_handler)
    service = CreateSkillService(users_repository, skills_repository)
    controller = CreateSkillController(service)
    view = CreateSkillView(controller)

    return view
