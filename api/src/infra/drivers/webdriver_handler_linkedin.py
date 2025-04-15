import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.domain.jobs.application.interfaces.webdriver_handler_linkedin_interface import (
    WebDriverHandlerLinkedinInterface,
)


class WebDriverHandlerLinkedin(WebDriverHandlerLinkedinInterface):
    """
    Class responsible for executing the LinkedIn access process.

    This class retrieves the LinkedIn company information from the repository
    and automates the browser to access the company's website.
    """

    def __init__(self) -> None:
        self.__webdriver: webdriver.Chrome = None

    def open_website(self, url: str) -> None:
        self.__webdriver = webdriver.Chrome()
        self.__webdriver.get(url)
        self.__webdriver.maximize_window()
        time.sleep(2)

    def log_in(self, email: str, password: str) -> None:
        self.__webdriver.find_element(By.LINK_TEXT, "Entrar").click()
        time.sleep(2)
        form_login = self.__webdriver.find_element(By.CLASS_NAME, "login__form")
        form_login.find_element(By.ID, "username").send_keys(email)
        time.sleep(1)
        form_login.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)

        form_login.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait confirmation 10 minutes
        WebDriverWait(self.__webdriver, 600).until(
            EC.presence_of_element_located((By.ID, "global-nav-search"))
        )

    def access_jobs(self) -> None:
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

        time.sleep(2)
        self.__webdriver.find_element(By.XPATH, "//a[text()='Remotas']").click()
        time.sleep(4)

    def get_total_pages(self) -> int:
        ul_paginator = self.__webdriver.find_element(
            By.CSS_SELECTOR,
            ".artdeco-pagination__pages.artdeco-pagination__pages--number",
        )
        list_pages = ul_paginator.find_elements(By.TAG_NAME, "li")
        return len(list_pages)

    def get_total_jobs(self) -> int:
        jobs = self.__webdriver.find_elements(
            By.CSS_SELECTOR,
            ".scaffold-layout__list > div > ul > li",
        )

        return len(jobs)

    def next_page(self, current_page: int) -> None:
        ul_paginator = self.__webdriver.find_element(
            By.CSS_SELECTOR,
            ".artdeco-pagination__pages.artdeco-pagination__pages--number",
        )
        list_pages = ul_paginator.find_elements(By.TAG_NAME, "li")
        for index in range(len(list_pages)):
            if index >= len(list_pages) or index == current_page:
                li = list_pages[index]
                li.find_element(By.TAG_NAME, "button").click()
                break

        return None

    def select_job(self, job_number) -> None:
        jobs = self.__webdriver.find_elements(
            By.CSS_SELECTOR,
            ".scaffold-layout__list > div > ul > li",
        )

        for index, job in enumerate(jobs):
            if index == job_number:
                div_job = job.find_element(By.TAG_NAME, "div")
                self.__webdriver.execute_script(
                    "arguments[0].scrollIntoView();", div_job
                )
                div_job.find_element(By.TAG_NAME, "div").click()
                time.sleep(2)
                break

    def check_simplified_application(self) -> bool:
        button_text = (
            WebDriverWait(self.__webdriver, 10)
            .until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "jobs-apply-button--top-card")
                )
            )
            .find_element(By.TAG_NAME, "button")
            .text
        )

        if "Candidatura simplificada" in button_text:
            return True

        return False

    def click_apply(self) -> None:
        WebDriverWait(self.__webdriver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "jobs-apply-button--top-card")
            )
        ).find_element(By.TAG_NAME, "button")

    def fill_contact_information(self, email, country_code, cellphone) -> None:
        pass
