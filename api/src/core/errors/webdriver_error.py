from datetime import datetime
from src.core.entities.error import Error


class WebdriverError(Error):
    """
    Custom exception to handle errors related to WebDriver.
    """

    def __init__(self, company_id: int, message: str) -> None:
        """
        Initializes a new instance of the WebdriverError class.

        Args:
            message (str): The error message to be displayed.
        """
        super().__init__(message)
        self.company_id = company_id
        self.message = message
        self.datetime = datetime.now()

    def __str__(self) -> str:
        """
        Returns a string representation of the WebDriver error.

        Returns:
            str: A string containing the error message.
        """
        return f"WebdriverError: CompanyId: {self.company_id}, message: {self.message}, datetime: {self.datetime}"
