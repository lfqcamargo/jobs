class HttpBadRequestError(Exception):
    """
    Exception raised for HTTP 400 Bad Request errors.

    Attributes:
        message (str): Description of the error.
        status_code (int): HTTP status code for the error (400).
        name (str): Name of the error ("BadRequest").
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the HttpBadRequestError with a specific message.

        Args:
            message (str): The error message describing the bad request.
        """
        super().__init__(message)
        self.status_code = 400
        self.name = "BadRequest"
        self.message = message
