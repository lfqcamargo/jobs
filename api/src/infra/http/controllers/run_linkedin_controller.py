from src.domain.jobs.application.services.run_linkedin_service import RunLinkedinService


class RunLinkedinController:
    """
    Controller responsible for handling requests related to the RunLinkedin service.

    This controller invokes the RunLinkedinService to execute the necessary actions related to
    the LinkedIn automation process.
    """

    def __init__(self, service: RunLinkedinService) -> None:
        """
        Initializes the RunLinkedinController with the given service.

        Args:
            service (RunLinkedinService): The service used to execute LinkedIn-related actions.
        """
        self.__service = service

    def handle(self) -> None:
        """
        Handles the execution of the RunLinkedinService.

        This method triggers the execution of the service, which performs the necessary
        operations on LinkedIn.

        Returns:
            None: This method does not return any value.
        """
        self.__service.execute()
