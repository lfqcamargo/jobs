class HttpUnprocessableEntityError(Exception):
    """
    Exception raised for HTTP 422 Unprocessable Entity errors.

    Attributes:
        message (str): Description of the error.
        status_code (int): HTTP status code for the error (422).
        name (str): Name of the error ("UnprocessableEntity").
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the HttpUnprocessableEntityError with a specific message.

        Args:
            message (str): The error message describing why the entity could not be processed.
        """
        super().__init__(message)
        self.status_code = 422
        self.name = "UnprocessableEntity"
        self.message = message
