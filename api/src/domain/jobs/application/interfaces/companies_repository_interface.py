from abc import ABC, abstractmethod
from src.domain.jobs.enterprise.entities.company import Company


class CompaniesRepositoryInterface(ABC):
    """
    Interface for the Companies Repository.

    This class defines the contract that any implementation of a Companies Repository
    must follow. It provides methods to retrieve company data.
    """

    @abstractmethod
    def find_by_name(self, name: str) -> Company | None:
        """
        Retrieve a company by its name.

        Returns:
            Company | None: The company instance if found, otherwise None.
        """

    @abstractmethod
    def find_all(self) -> list[Company] | None:
        """
        Retrieve all companies.

        Returns:
            list[Company] | None: A list of company instances if available, otherwise None.
        """
