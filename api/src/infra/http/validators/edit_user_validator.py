from typing import Optional
from pydantic import BaseModel, ValidationError, EmailStr, Field
from src.infra.http.views.http_types.http_request import HttpRequest


def edit_user_validator(http_request: HttpRequest) -> None:
    """
    Validates the user data for editing in the given HTTP request.

    Args:
        http_request (HttpRequest): The HTTP request containing the user data.

    Raises:
        ValidationError: If the validation fails for any of the fields.
    """

    class BodyData(BaseModel):
        """
        Validate Body Schema for Editing User
        """

        name: Optional[str] = Field(min_length=3, max_length=50, default=None)
        email: Optional[EmailStr] = Field(default=None)
        password: Optional[str] = Field(min_length=8, max_length=100, default=None)
        birthday_date: Optional[str] = Field(min_length=10, max_length=10, default=None)

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error

    curriculum = http_request.files.get("curriculum")
    if curriculum:
        if curriculum.mimetype != "application/pdf":
            raise ValueError("Curriculum must be a PDF file.")

    if "identifier" not in http_request.params:
        raise ValueError("User ID is required for editing.")
