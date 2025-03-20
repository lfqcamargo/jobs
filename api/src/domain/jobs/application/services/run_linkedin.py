import time
import os
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.domain.jobs.application.interfaces.companies_repository_interface import (
    CompaniesRepositoryInterface,
)
from src.core.errors.webdriver_error import WebdriverError
from src.domain.users.application.interfaces.users_repository_interface import (
    UsersRepositoryInterface,
)

from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)


class RunLinkedin:
    """
    Class responsible for executing the LinkedIn access process.

    This class retrieves the LinkedIn company information from the repository
    and automates the browser to access the company's website.
    """

    def __init__(
        self,
        companies_repository: CompaniesRepositoryInterface,
        user_repository: UsersRepositoryInterface,
        password_handler: PasswordHandlerInterface,
    ) -> None:
        """
        Initializes the RunLinkedin process.

        Args:
            companies_repository (CompaniesRepositoryInterface): The repository to
            retrieve company information.
            user_repository (UsersRepositoryInterface): The repository to retrieve user information.
            password_handler (PasswordHandlerInterface): Driver to manage user password.
        """
        self.__companies_repository = companies_repository
        self.__user_repository = user_repository
        self.__password_handler = password_handler
        self.__webdriver = webdriver.Chrome()
        self.__linkedin = self.__companies_repository.find_by_name("Linkedin")

    def execute(self) -> None:
        """
        Executes the LinkedIn access process.
        """
        self.__access_website()
        self.__log_in()
        self.__access_jobs()
        self.__find_jobs()

    def __access_website(self) -> None:
        try:
            self.__webdriver.get(self.__linkedin.get_link())
            self.__webdriver.maximize_window()
            time.sleep(2)
        except Exception as e:
            raise WebdriverError(
                company_id=self.__linkedin.get_identifier(),
                message="Error when trying to access the linkedin website",
            ) from e

    def __log_in(self) -> None:
        user = self.__get_user()
        if not user:
            raise WebdriverError(
                company_id=self.__linkedin.get_identifier(),
                message="Error when trying to log in",
            )

        try:
            self.__webdriver.find_element(By.LINK_TEXT, "Entrar").click()
            time.sleep(2)
            form_login = self.__webdriver.find_element(By.CLASS_NAME, "login__form")
            form_login.find_element(By.ID, "username").send_keys(user.get_email())
            form_login.find_element(By.ID, "password").send_keys(
                self.__password_handler.decrypt_password(user.get_password())
            )
            form_login.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            # Wait confirmation 10 minutes
            WebDriverWait(self.__webdriver, 600).until(
                EC.presence_of_element_located((By.ID, "global-nav-search"))
            )
        except Exception as e:
            raise WebdriverError(
                company_id=self.__linkedin.get_identifier(),
                message="Error when trying to log in",
            ) from e

    def __access_jobs(self) -> None:
        try:
            self.__webdriver.find_element(By.CSS_SELECTOR, "a[href*='jobs']").click()
            WebDriverWait(self.__webdriver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "jobs-home-vertical-list__entity-list")
                )
            )
            div_a = self.__webdriver.find_element(
                By.CLASS_NAME, "discovery-templates-vertical-list__footer"
            )
            div_a.find_element(By.TAG_NAME, "a").click()

            # Wait load
            WebDriverWait(self.__webdriver, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "scaffold-layout__list-detail-container")
                )
            )

        except Exception as e:
            raise e

    def __find_jobs(self) -> None:
        while True:
            try:
                self.__jobs_simplified()
            except Exception as e:
                raise WebdriverError(
                    company_id=self.__linkedin.get_identifier(),
                    message="Error when trying to access the linkedin jobs simplified",
                ) from e

    def __jobs_simplified(self) -> None:
        self.__webdriver.find_element(
            By.XPATH, "//a[text()='Candidatura simplificada']"
        ).click()
        time.sleep(4)

        self.__scroll_jobs()

        # list_jobs = self.__get_list_jobs()

        # for item in list_jobs:
        #     div_element = item.find_element(By.TAG_NAME, "div")
        #     div_element.find_element(By.TAG_NAME, "div").click()
        #     time.sleep(2)
        #     try:
        #         self.__apply_simplified()
        #     except Exception:
        #         self.__webdriver.find_element(
        #             By.CSS_SELECTOR, 'button[aria-label="Fechar"]'
        #         ).click()
        #         self.__webdriver.find_element(
        #             By.CSS_SELECTOR,
        #             'button[data-control-name="discard_application_confirm_btn"]',
        #         ).click()
        #         continue

    def __scroll_jobs(self) -> None:
        while True:
            list_pages = self.__get_list_pages()
            for index in range(len(list_pages)):
                list_pages = self.__get_list_pages()
                if index >= len(list_pages):
                    break
                li = list_pages[index]
                try:
                    li.find_element(By.TAG_NAME, "button").click()
                    time.sleep(2)
                    list_jobs = self.__get_list_jobs()
                    for job in list_jobs:
                        div_element = job.find_element(By.TAG_NAME, "div")
                        self.__webdriver.execute_script(
                            "arguments[0].scrollIntoView();", div_element
                        )
                        div_element.find_element(By.TAG_NAME, "div").click()
                        time.sleep(2)
                        try:
                            self.__apply_simplified()
                        except Exception:
                            self.__webdriver.find_element(
                                By.CSS_SELECTOR, 'button[aria-label="Fechar"]'
                            ).click()
                            self.__webdriver.find_element(
                                By.CSS_SELECTOR,
                                'button[data-control-name="discard_application_confirm_btn"]',
                            ).click()
                            continue
                except Exception as e:
                    print(e)

    def __apply_simplified(self) -> None:
        WebDriverWait(self.__webdriver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "jobs-apply-button--top-card")
            )
        ).find_element(By.TAG_NAME, "button").click()
        time.sleep(2)
        self.__select_curriculum()
        self.__fill_out_form()

    def __fill_out_form(self) -> None:
        try:
            divs_input: list[WebElement] = WebDriverWait(self.__webdriver, 10).until(
                EC.presence_of_all_elements_located(
                    (
                        By.CSS_SELECTOR,
                        ".artdeco-text-input--container.ember-view",
                    )
                )
            )

            for divs in divs_input:
                label = divs.find_element(By.TAG_NAME, "label").text
                input_container = divs.find_element(By.TAG_NAME, "input")
                time.sleep(1)
                input_container.send_keys(self.__get_input_response(label))

        except Exception:
            pass

    def __select_curriculum(self) -> None:
        WebDriverWait(self.__webdriver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view",
                )
            )
        ).click()

        label = WebDriverWait(self.__webdriver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".jobs-document-upload-redesign-card__toggle-label.t-bold",
                )
            )
        )
        radio_button = label.find_element(
            By.XPATH, "./preceding-sibling::input[@type='radio']"
        )
        if not radio_button.is_selected():
            label.click()
        time.sleep(2)

        WebDriverWait(self.__webdriver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view",
                )
            )
        ).click()
        time.sleep(2)

    def __get_input_response(self, label: str) -> any:
        pass

    def __get_list_pages(self) -> list[WebElement]:
        ul_paginator = self.__webdriver.find_element(
            By.CSS_SELECTOR,
            ".artdeco-pagination__pages.artdeco-pagination__pages--number",
        )
        list_pages = ul_paginator.find_elements(By.TAG_NAME, "li")
        return list_pages

    def __get_list_jobs(self) -> list[WebElement]:
        return self.__webdriver.find_elements(
            By.CSS_SELECTOR,
            ".scaffold-layout__list > div > ul > li",
        )

    def __get_user(self) -> User:
        return self.__user_repository.find_by_email(os.getenv("EMAIL"))
