from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.companies_repository import (
    CompaniesRepository,
)
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.infra.drivers.password_handler import PasswordHandler
from src.infra.http.controllers.run_linkedin_controller import RunLinkedinController
from src.infra.http.views.run_linkedin_view import RunLinkedinView

from src.domain.jobs.application.services.run_linkedin_service import RunLinkedinService


def run_linkedin_composer() -> RunLinkedinView:
    """
    Composer function to create and return a RunLinkedinService instance.

    This function initializes all the necessary dependencies for the RunLinkedinService, including
    the CompaniesRepository, UsersRepository, PasswordHandler, and the RunLinkedinService itself.
    It then ties everything together into a complete setup, providing the appropriate controller
    and view for handling LinkedIn automation requests.

    Returns:
        RunLinkedinView: The fully initialized RunLinkedinView instance, ready handle HTTP requests.
    """
    companies_repository = CompaniesRepository(db_connection_handler)
    users_repository = UsersRepository(db_connection_handler)
    password_handler = PasswordHandler()
    service = RunLinkedinService(
        companies_repository, users_repository, password_handler
    )
    controller = RunLinkedinController(service)
    view = RunLinkedinView(controller)

    return view
