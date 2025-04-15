from src.domain.users.application.interfaces.users_repository_interface import (
    UsersRepositoryInterface,
)
from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)
from src.domain.jobs.application.interfaces.companies_repository_interface import (
    CompaniesRepositoryInterface,
)
from src.domain.jobs.application.interfaces.questions_repository_interface import (
    QuestionsRepositoryInterface,
)
from src.domain.jobs.application.interfaces.webdriver_handler_linkedin_interface import (
    WebDriverHandlerLinkedinInterface,
)
from src.domain.users.enterprise.entities.user import User
from src.domain.jobs.enterprise.entities.company import Company


class RunLinkedinService:
    """
    Class responsible for executing the LinkedIn access process.

    This class retrieves the LinkedIn company information from the repository
    and automates the browser to access the company's website.
    """

    def __init__(
        self,
        companies_repository: CompaniesRepositoryInterface,
        users_repository: UsersRepositoryInterface,
        password_handler: PasswordHandlerInterface,
        questions_repository: QuestionsRepositoryInterface,
        webdriver_handler: WebDriverHandlerLinkedinInterface,
    ) -> None:
        self.__companies_repository = companies_repository
        self.__users_repository = users_repository
        self.__password_handler = password_handler
        self.__questions_repository = questions_repository
        self.__webdriver = webdriver_handler
        self.__simplified = True

        self.__user: User = None
        self.__company: Company = None

    def execute(self, user_id: int, simplified: bool = True) -> None:
        """
        Run Linkedin
        """
        self.__user = self.__users_repository.find_by_identifier(user_id)
        self.__company = self.__companies_repository.find_by_name("Linkedin")
        self.__simplified = simplified

        self.__access_jobs_remote()
        self.__apply_jobs()

    def __access_jobs_remote(self) -> None:
        try:
            self.__webdriver.open_website(self.__company.get_link())
        except Exception as e:
            print(e)
            raise e

        try:
            email: str = self.__user.get_email()
            password: str = self.__password_handler.decrypt_password(
                self.__user.get_password()
            )
            self.__webdriver.log_in(email, password)
        except Exception as e:
            print(e)
            raise e

        try:
            self.__webdriver.access_jobs()
        except Exception as e:
            print(e)
            raise e

    def __apply_jobs(self) -> None:
        total_pages: int = self.__webdriver.get_total_pages()

        for page in range(total_pages):
            total_jobs: int = self.__webdriver.get_total_jobs()

            for job_number in range(total_jobs):
                self.__webdriver.select_job(job_number)

                is_simplified = self.__webdriver.check_simplified_application()

                if self.__simplified is True and is_simplified is True:
                    self.__apply_job()
                else:
                    continue

            self.__webdriver.next_page()

    def __apply_job(self) -> None:
        self.__webdriver.click_apply()

        try:
            self.__webdriver.fill_contact_information()
        except Exception as e:
            print("Erro ao Tentar Preencher Informações de Contato.")
            print(e)
