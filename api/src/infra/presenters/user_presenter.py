import base64
from src.domain.users.enterprise.entities.user import User


class UserPresenter:
    """
    Presenter responsible for transforming a User entity into an HTTP-friendly format.

    This class provides a method to convert a User object into a dictionary
    that can be easily serialized into JSON responses.
    """

    @staticmethod
    def to_http(user: User) -> dict:
        """
        Converts a User entity into a dictionary representation.

        Args:
            user (User): The User entity to be transformed.

        Returns:
            dict: A dictionary containing the user's identifier, name, email,
            and other relevant fields.
        """
        return {
            "id": user.get_identifier(),
            "name": user.get_name(),
            "email": user.get_email(),
            "birthday_date": user.get_birthday_date(),
            "curriculum": base64.b64encode(user.get_curriculum()).decode("utf-8"),
        }
