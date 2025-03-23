from datetime import datetime
from pydantic import BaseModel, ValidationError, EmailStr, Field


def edit_user_validator(
    identifier: int, name: str, email: str, birthday_date: str, password: str | None
) -> None:
    """
    Validates the user data for edit a user.

    This function validates the user's name, email, birthday date, and password fields
    according to predefined rules. If any of the fields are invalid, it raises a validation error.

    Args:
        identifier (int): The identifier of the user to be edited.
        name (str): The user's name. Must be between 3 and 50 characters.
        email (str): The user's email. Should be a valid email format.
        birthday_date (str): The user's birthday date in 'YYYY-MM-DD' format.
        password (str | None): The user's password. Must be a valid string if provided.

    Raises:
        ValidationError: If any of the fields fail the validation checks.
        ValueError: If the birthday date is not in the correct format ('YYYY-MM-DD').
    """

    class BodyData(BaseModel):
        """
        Validate the schema of user data.

        Attributes:
            identifier (int): User's identifier.
            name (str): User's name, must be between 3 and 50 characters.
            email (EmailStr): User's email address.
            password (str | None): User's password (optional).
            birthday_date (str): User's birthday date, must be in 'YYYY-MM-DD' format.
        """

        identifier: int = Field(..., gt=0)
        name: str = Field(..., min_length=3, max_length=50)
        email: EmailStr
        password: str | None = Field(...)  # Optional password field
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
        BodyData(
            identifier=identifier,
            name=name,
            email=email,
            password=password,
            birthday_date=birthday_date,
        )
    except ValidationError as error:
        raise error
    except ValueError as error:
        raise error
