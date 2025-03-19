from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.companies_repository import (
    CompaniesRepository,
)
from src.infra.http.controllers.fetch_companies_controller import (
    FetchCompaniesController,
)
from src.infra.http.views.fetch_companies_view import FetchCompaniesView
from src.domain.jobs.application.services.fetch_companies_services import (
    FetchCompaniesService,
)


def fetch_companies_composer() -> FetchCompaniesView:
    """
    Composer function to create and return a RunLinkedin instance.

    This function initializes the necessary dependencies, the CompaniesRepository,
    User, and returns a fully constructed RunLinkedin instance.

    Returns:
        RunLinkedin: The initialized RunLinkedin instance.
    """
    companies_repository = CompaniesRepository(db_connection_handler)
    service = FetchCompaniesService(companies_repository)
    controller = FetchCompaniesController(service)
    view = FetchCompaniesView(controller)

    return view
