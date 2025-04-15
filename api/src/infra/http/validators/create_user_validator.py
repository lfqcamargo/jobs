from pydantic import BaseModel, ValidationError, EmailStr, Field
from src.infra.http.views.http_types.http_request import HttpRequest


def create_user_validator(http_request: HttpRequest) -> None:
    """
    Validates the user data in the given HTTP request.

    Args:
        http_request (HttpRequest): The HTTP request containing the user data.

    Raises:
        ValidationError: If the validation fails for any of the fields.
    """

    class BodyData(BaseModel):
        """
        Validate Body Schema
        """

        name: str = Field(..., min_length=3, max_length=50)
        email: EmailStr
        password: str = Field(..., min_length=8, max_length=100)
        birthday_date: str = Field(..., min_length=10, max_length=10)
        country_code: str = Field(..., min_length=2, max_length=2)
        phone_number: str = Field(..., min_length=11, max_length=11)

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error

    curriculum = http_request.files
    if not curriculum:
        raise ValueError("Curriculum file is required.")

    if curriculum.mimetype != "application/pdf":
        raise ValueError("Curriculum must be a PDF file.")
