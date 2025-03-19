from src.domain.jobs.application.interfaces.companies_repository_interface import (
    CompaniesRepositoryInterface,
)
from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.infra.database.postgres.models.company_model import CompanyModel
from src.domain.jobs.enterprise.entities.company import Company
from src.infra.database.postgres.mappers.company_mapper import CompanyMapper


class CompaniesRepository(CompaniesRepositoryInterface):
    """
    Repository class for managing Company data in a PostgreSQL database.

    This class implements the CompaniesRepositoryInterface and provides methods
    to retrieve company records from the database.
    """

    def __init__(self, db_connection: DBConnectionHandlerInterface) -> None:
        self.__db_connection = db_connection

    def find_by_name(self, name: str) -> Company | None:
        with self.__db_connection as database:
            company_model = (
                database.session.query(CompanyModel)
                .filter(CompanyModel.name == name)
                .first()
            )
            if company_model:
                return CompanyMapper.to_domain(company_model)
            return None

    def find_all(self) -> list[Company] | None:
        with self.__db_connection as database:
            companies_model = database.session.query(CompanyModel).all()
            if companies_model:
                companies = []
                for company in companies_model:
                    companies.append(CompanyMapper.to_domain(company))

                return companies
            return None
