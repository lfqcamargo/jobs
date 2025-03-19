class AlreadyExistsError(Exception):
    """
    Exception raised when a user with the same email or nickname already exists.

    Attributes:
        message (str): Explanation of the error.
        field (str): Field to error
    """

    def __init__(self, message: str, field: str) -> None:
        """
        Initializes the AlreadyExistsError with a specific message.

        Args:
            message (str): The error message to describe the exception.
            field (str): Field to error
        """
        super().__init__(message)
        self.message = message
        self.name = "AlreadyExistsError"
        self.field = field

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> dict:
        """
        Converts the error into a dictionary for JSON serialization.
        """
        return {"title": self.name, "detail": self.message, "field": self.field}
