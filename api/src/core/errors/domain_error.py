class DomainError(Exception):
    """
    Exception raised for general error domains.

    Attributes:
        message (str): Explanation of the domain.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the DomainError with a specific message.

        Args:
            message (str): The domain message to describe the exception.
        """
        super().__init__(message)
        self.message = message
        self.name = "DomainError"

    def __str__(self):
        return self.message

    def to_dict(self):
        """
        Converts the domain into a dictionary for JSON serialization.
        """
        return {"title": self.name, "detail": self.message}
