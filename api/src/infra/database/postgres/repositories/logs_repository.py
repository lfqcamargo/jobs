from src.infra.middlewares.interfaces.logs_repository_interface import (
    LogsRepositoryInterface,
)
from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.core.errors.webdriver_error import WebdriverError
from src.infra.database.postgres.models.logs_model import LogsModel


class LogsRepository(LogsRepositoryInterface):
    """
    Repository class for managing Company data in a PostgreSQL database.

    This class implements the LogsRepositoryInterface and provides methods
    to retrieve company records from the database.
    """

    def __init__(self, db_connection: DBConnectionHandlerInterface) -> None:
        self.__db_connection = db_connection

    def save_webdriver_error(self, error: WebdriverError) -> None:
        with self.__db_connection as database:
            log = LogsModel(
                description=error.message,
                type="WebdriverError",
                datetime=error.datetime,
                company_id=error.company_id,
            )

            database.session.add(log)
            database.session.commit()
