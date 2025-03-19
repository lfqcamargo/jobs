from src.infra.database.postgres.models.company_model import CompanyModel
from src.domain.jobs.enterprise.entities.company import Company
from src.domain.jobs.application.dto.create_company_dto import CreateCompanyDTO


class CompanyMapper:
    """
    Mapper class for converting between CompanyModel (database model) and Company (domain entity).
    """

    @staticmethod
    def to_domain(raw: CompanyModel) -> Company:
        """
        Converts a CompanyModel instance to a Company domain entity.

        Args:
            raw (CompanyModel): The database model instance representing a company.

        Returns:
            Company: A domain entity representing the company.
        """
        dto = CreateCompanyDTO(name=raw.name, link=raw.link, identifier=raw.id)
        return Company.create(dto)
