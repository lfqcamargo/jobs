from src.core.entities.entity import Entity
from src.domain.jobs.application.dto.create_company_dto import CreateCompanyDTO


class Company(Entity):
    """
    Represents a company entity.

    This class extends the base Entity class and includes specific attributes
    and methods related to a company.
    """

    def __init__(self, name: str, link: str, identifier: int = 0) -> None:
        """
        Initializes a Company instance.

        Args:
            name (str): The name of the company.
            link (str): The link website of the company.
            identifier (int, optional): The unique identifier of the company. Defaults to 0.
        """
        super().__init__(identifier)
        self.__name = name
        self.__link = link

    def get_name(self) -> str:
        """
        Retrieve the company's name.

        Returns:
            str: The name of the company.
        """
        return self.__name

    def get_link(self) -> str:
        """
        Retrieve the company's link.

        Returns:
            str: The link of the company.
        """
        return self.__link

    @staticmethod
    def create(props: CreateCompanyDTO) -> "Company":
        """
        Factory method to create a new Company instance from a DTO.

        Args:
            props (CreateCompanyDTO): Data Transfer Object containing company details.

        Returns:
            Company: A new instance of Company with the given properties.
        """
        company: Company = Company(
            name=props.name, link=props.link, identifier=props.identifier
        )

        return company

    def __str__(self) -> str:
        """
        Returns a string representation of the company.

        Returns:
            str: A formatted string containing company details.
        """
        return f"ID: {self.__identifier}, name: {self.__name}, link: {self.__link}"
