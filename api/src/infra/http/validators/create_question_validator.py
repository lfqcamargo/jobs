from typing import Optional
from pydantic import BaseModel, ValidationError, Field
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes
from src.infra.http.views.http_types.http_request import HttpRequest


def create_question_validator(http_request: HttpRequest) -> None:
    """
    Validates the question data in the given HTTP request.

    Args:
        http_request (HttpRequest): The HTTP request containing the question data.

    Raises:
        ValidationError: If validation fails for any of the fields in the request body.
        ValueError: If the user ID or company ID is missing from the request parameters.
    """

    class BodyData(BaseModel):
        """
        Schema for validating the question creation body payload.
        """

        question: str = Field(
            ..., min_length=3, max_length=255, description="The content of the question"
        )
        response: str = Field(
            ...,
            min_length=3,
            max_length=255,
            description="The response to the question",
        )
        question_type: QuestionTypes = Field(
            ..., description="The type of the question (e.g., text, number, date)"
        )
        date_time: str = Field(
            ..., description="The timestamp when the question was asked (ISO format)"
        )

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error

    if "user_id" not in http_request.params:
        raise ValueError("user ID is required to create a question.")

    if "company_id" not in http_request.params:
        raise ValueError("company ID is required to create a question.")
