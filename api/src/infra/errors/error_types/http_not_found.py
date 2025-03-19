class HttpNotFoundError(Exception):
    """
    Exception raised for HTTP 404 Not Found errors.

    Attributes:
        message (str): Description of the error.
        status_code (int): HTTP status code for the error (404).
        name (str): Name of the error ("NotFound").
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the HttpNotFoundError with a specific message.

        Args:
            message (str): The error message describing the resource not found.
        """
        super().__init__(message)
        self.status_code = 404
        self.name = "NotFound"
        self.message = message
