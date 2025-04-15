import threading
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.domain_error import DomainError
from src.domain.jobs.application.controllers.interfaces.run_linkedin_controller_interface import (
    RunLinkedinControllerInterface,
)
from src.domain.jobs.application.services.run_linkedin_service import RunLinkedinService


class RunLinkedinController(RunLinkedinControllerInterface):
    """
    Controller responsible for handling the execution of the LinkedIn process.

    This controller receives a user ID, starts a background thread to run the
    LinkedIn service execution asynchronously, and handles possible domain errors.

    Attributes:
        __service (RunLinkedinService): Service that contains the LinkedIn execution logic.
    """

    def __init__(self, service: RunLinkedinService) -> None:
        self.__service = service

    def handle(
        self,
        user_id: int,
    ) -> None:
        def target() -> None:
            result = self.__service.execute(user_id)

            if isinstance(result, Exception):
                if isinstance(result, ResourceNotFoundError):
                    raise result
                if isinstance(result, DomainError):
                    raise result
                raise DomainError("An unexpected domain error occurred.")

        thread = threading.Thread(target=target)
        thread.start()

        return None
