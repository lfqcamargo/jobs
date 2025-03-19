class HttpConficlitError(Exception):
    """
    Exception raised for HTTP 409 Conflict errors.

    Attributes:
        message (str): Description of the error.
        status_code (int): HTTP status code for the error (409).
        name (str): Name of the error ("Conficlit").
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the HttpConficlitError with a specific message.

        Args:
            message (str): The error message describing the conflict.
        """
        super().__init__(message)
        self.status_code = 409
        self.name = "Conficlit"
        self.message = message
