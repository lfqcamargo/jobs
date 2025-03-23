from datetime import datetime
from pydantic import BaseModel, ValidationError, EmailStr, Field


def create_user_validator(
    name: str, email: str, birthday_date: str, password: str
) -> None:
    """
    Validates the user data for creating a new user.

    Args:
        name (str): The user's name.
        email (str): The user's email.
        birthday_date (str): The user's birthday date in 'YYYY-MM-DD' format.
        password (str): The user's password.

    Raises:
        ValidationError: If the validation fails for any of the fields.
        ValueError: If the birthday_date is not in the correct format.
    """

    class BodyData(BaseModel):
        """
        Validate the schema of user data.
        """

        name: str = Field(..., min_length=3, max_length=50)
        email: EmailStr
        password: str = Field(..., min_length=8, max_length=100)
        birthday_date: str = Field(..., min_length=8)

        @classmethod
        def validate_birthday_date(cls, v: str) -> str:
            """
            Validates the birthday date format.

            Args:
                v (str): The birthday date to validate, expected format 'YYYY-MM-DD'.

            Raises:
                ValueError: If the birthday date is not in the correct format.
            """
            try:
                datetime.strptime(v, "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError(
                    "Birthday date must be in 'YYYY-MM-DD' format."
                ) from exc
            return v

    try:

        BodyData(name=name, email=email, password=password, birthday_date=birthday_date)
    except ValidationError as error:
        raise error
    except ValueError as error:
        raise error
