from src.domain.jobs.application.services.fetch_companies_services import (
    FetchCompaniesService,
)
from src.infra.http.presenters.company_presenter import CompanyPresenter


class FetchCompaniesController:
    """
    Controller responsible for handling the process of fetching companies.

    This class interacts with the FetchCompaniesService to retrieve a list of companies
    and formats the output using the CompanyPresenter.
    """

    def __init__(self, service: FetchCompaniesService) -> None:
        """
        Initializes the FetchCompaniesController with a service.

        Args:
            service (FetchCompaniesService): The service responsible for fetching companies.
        """
        self.__serivce = service

    def handle(self) -> dict:
        """
        Handles the request to fetch companies.

        Calls the service to retrieve companies and transforms them into an HTTP-friendly format.

        Returns:
            dict: A dictionary containing the list of companies in the expected response format.
        """
        companies = self.__serivce.execute()

        return {"companies": list(map(CompanyPresenter.to_http, companies))}
