class WrongCredentialsError(Exception):
    """
    Exception raised when a user with the same email or nickname already exists.

    Attributes:
        message (str): Explanation of the error.
        resource (str): Resource to error
    """

    def __init__(self) -> None:
        """
        Initializes the WrongCredentialsError with a specific message.

        Args:
            message (str): The error message to describe the exception.
            resource (str): Resource to error
        """
        self.message = "Wrong Credentials"
        self.name = "WrongCredentialsError"

    def __str__(self):
        return self.message

    def to_dict(self):
        """
        Converts the error into a dictionary for JSON serialization.
        """
        return {"title": self.name, "detail": self.message}
