from src.domain.jobs.application.interfaces.companies_repository_interface import (
    CompaniesRepositoryInterface,
)
from src.domain.jobs.enterprise.entities.company import Company


class FetchCompaniesService:
    def __init__(self, companies_repository: CompaniesRepositoryInterface) -> None:
        self.__companies_repository = companies_repository

    def execute(self) -> list[Company] | None:
        return self.__companies_repository.find_all()
