class ResourNotFoundError(Exception):
    """
    Exception raised when a user with the same email or nickname already exists.

    Attributes:
        message (str): Explanation of the error.
        resource (str): Resource to error
    """

    def __init__(self, message: str, resource: str) -> None:
        """
        Initializes the ResourNotFoundError with a specific message.

        Args:
            message (str): The error message to describe the exception.
            resource (str): Resource to error
        """
        super().__init__(message)
        self.message = message
        self.name = "ResourNotFoundError"
        self.resource = resource

    def __str__(self):
        return self.message

    def to_dict(self):
        """
        Converts the error into a dictionary for JSON serialization.
        """
        return {"title": self.name, "detail": self.message, "resource": self.resource}
