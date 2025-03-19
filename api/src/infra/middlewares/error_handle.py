from functools import wraps
from src.core.errors.webdriver_error import WebdriverError
from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.database.postgres.repositories.logs_repository import LogsRepository


def error_handler(func):
    """
    Middleware to catch and handle WebdriverError.
    It allows centralizing error handling for specific exceptions.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except WebdriverError as e:
            log = LogsRepository(db_connection_handler)
            log.save_webdriver_error(e)

    return wrapper
