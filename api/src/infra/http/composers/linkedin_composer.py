from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.companies_repository import (
    CompaniesRepository,
)
from src.infra.database.postgres.repositories.users_repository import UsersRepository
from src.infra.drivers.password_handler import PasswordHandler

from src.domain.jobs.application.services.run_linkedin import RunLinkedin


def linkedin_composer() -> RunLinkedin:
    """
    Composer function to create and return a RunLinkedin instance.

    This function initializes the necessary dependencies, the CompaniesRepository,
    User, and returns a fully constructed RunLinkedin instance.

    Returns:
        RunLinkedin: The initialized RunLinkedin instance.
    """
    companies_repository = CompaniesRepository(db_connection_handler)
    users_repository = UsersRepository(db_connection_handler)
    password_handler = PasswordHandler()

    linkedin = RunLinkedin(companies_repository, users_repository, password_handler)

    return linkedin
