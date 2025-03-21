class HttpValidationParamError(Exception):
    """
    Custom error to indicate that validation failed for parameters.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the HttpValidationParamError with a specific message.

        Args:
            message (str): The error message describing why the parameters are invalid.
        """
        super().__init__(message)
        self.status_code = 400
        self.name = "ValidationParamError"
        self.message = message
