class ErrorServer(Exception):
    """
    Exception raised for general server errors.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the ErrorServer with a specific message.

        Args:
            message (str): The error message to describe the exception.
        """
        super().__init__(message)
        self.message = message
        self.name = "ErrorServer"

    def __str__(self):
        return self.message

    def to_dict(self):
        """
        Converts the error into a dictionary for JSON serialization.
        """
        return {"title": self.name, "detail": self.message}
