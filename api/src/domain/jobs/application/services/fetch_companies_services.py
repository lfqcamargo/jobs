from src.domain.jobs.application.interfaces.companies_repository_interface import (
    CompaniesRepositoryInterface,
)
from src.domain.jobs.enterprise.entities.company import Company


class FetchCompaniesService:
    """
    Service responsible for fetching companies from the repository.

    This service interacts with the CompaniesRepositoryInterface to retrieve a list of companies
    and returns them in the form of Company entities.
    """

    def __init__(self, companies_repository: CompaniesRepositoryInterface) -> None:
        """
        Initializes the FetchCompaniesService with a repository.

        Args:
            companies_repository (CompaniesRepositoryInterface): The repository used
            to fetch companies.
        """
        self.__companies_repository = companies_repository

    def execute(self) -> list[Company] | None:
        """
        Executes the service to retrieve a list of companies.

        Interacts with the repository to fetch all companies.

        Returns:
            list[Company] | None: A list of Company entities, or None if no companies are found.
        """
        return self.__companies_repository.find_all()
