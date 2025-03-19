from abc import ABC, abstractmethod
from src.core.errors.webdriver_error import WebdriverError


class LogsRepositoryInterface(ABC):

    @abstractmethod
    def save_webdriver_error(self, error: WebdriverError) -> None:
        pass
