from src.domain.jobs.application.services.run_linkedin_service import RunLinkedinService
from src.domain.jobs.application.controllers.run_linkedin_controller import (
    RunLinkedinController,
)
from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.companies_repository import (
    CompaniesRepository,
)
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.infra.database.postgres.repositories.questions_repository import (
    QuestionsRepository,
)
from src.infra.drivers.password_handler import PasswordHandler
from src.infra.drivers.webdriver_handler_linkedin import WebDriverHandlerLinkedin

from src.infra.http.views.run_linkedin_view import RunLinkedinView


def run_linkedin_composer() -> RunLinkedinView:
    """
    Composer function to create and return a RunLinkedinView instance.

    This function initializes all required dependencies for the LinkedIn automation process,
    including repositories, password handler, and WebDriver handler. It ties all components
    together to create a fully functional service responsible for accessing LinkedIn
    company profiles.

    Returns:
        RunLinkedinView: The initialized service ready to automate LinkedIn access
        and interaction.
    """
    companies_repository = CompaniesRepository(db_connection_handler)
    users_repository = UsersRepository(db_connection_handler)
    questions_repository = QuestionsRepository(db_connection_handler)
    password_handler = PasswordHandler()
    webdriver_handler = WebDriverHandlerLinkedin()
    service = RunLinkedinService(
        companies_repository,
        users_repository,
        password_handler,
        questions_repository,
        webdriver_handler,
    )
    controller = RunLinkedinController(service)
    view = RunLinkedinView(controller)

    return view
