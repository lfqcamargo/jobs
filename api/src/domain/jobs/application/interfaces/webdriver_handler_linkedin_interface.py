from abc import ABC, abstractmethod


class WebDriverHandlerLinkedinInterface(ABC):
    """
    Class responsible for executing the LinkedIn access process.

    This class retrieves the LinkedIn company information from the repository
    and automates the browser to access the company's website.
    """

    @abstractmethod
    def open_website(self, url: str) -> None:
        """
        Opens the specified website.

        Args:
            url (str): The URL of the website to open.

        Returns:
            None
        """

    @abstractmethod
    def log_in(self, email: str, password: str) -> None:
        """
        Logs in to LinkedIn with the provided credentials.

        Args:
            email (str): User email address.
            password (str): User password.

        Returns:
            None
        """

    @abstractmethod
    def access_jobs(self) -> None:
        """
        Accesses the LinkedIn jobs section.

        Returns:
            None
        """

    @abstractmethod
    def get_total_pages(self) -> int:
        """
        Get Total Pages

        Returns: int
        """

    @abstractmethod
    def get_total_jobs(self) -> int:
        """
        Get Total Jobs

        Returns: None
        """

    @abstractmethod
    def next_page(self, current_page: int) -> None:
        """
        Go Next Page

        Returns: None
        """

    @abstractmethod
    def select_job(self, job_number: int) -> None:
        """
        Select Job

        Returns: None
        """

    @abstractmethod
    def check_simplified_application(self) -> bool:
        """
        Check Simplified Application

        Returns: Boolean
        """

    @abstractmethod
    def click_apply(self) -> None:
        """
        Click Apply

        Returns: None
        """

    @abstractmethod
    def fill_contact_information(
        self, email: str, country_code: str, cellphone: str
    ) -> None:
        """
        Fill in Contact Information
        """
