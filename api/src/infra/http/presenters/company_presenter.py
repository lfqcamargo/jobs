from src.domain.jobs.enterprise.entities.company import Company


class CompanyPresenter:
    """
    Presenter responsible for transforming a Company entity into an HTTP-friendly format.

    This class provides a method to convert a Company object into a dictionary
    that can be easily serialized into JSON responses.
    """

    @staticmethod
    def to_http(company: Company) -> dict:
        """
        Converts a Company entity into a dictionary representation.

        Args:
            company (Company): The Company entity to be transformed.

        Returns:
            dict: A dictionary containing the company's identifier, name, and link.
        """
        return {
            "id": company.get_identifier(),
            "name": company.get_name(),
            "link": company.get_link(),
        }
