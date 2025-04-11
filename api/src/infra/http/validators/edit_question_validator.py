from typing import Optional
from pydantic import BaseModel, ValidationError, Field
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes
from src.infra.http.views.http_types.http_request import HttpRequest


def edit_question_validator(http_request: HttpRequest) -> None:
    """
    Validates the question data in the given HTTP request for editing a question.

    Args:
        http_request (HttpRequest): The HTTP request containing the question data.

    Raises:
        ValidationError: If validation fails for any of the fields in the request body.
        ValueError: If the question ID is missing from the request parameters.
    """

    class BodyData(BaseModel):
        """
        Schema for validating the question editing body payload.
        """

        question: Optional[str] = Field(min_length=3)
        response: Optional[str]
        question_type: Optional[QuestionTypes]
        date_time: Optional[str]

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error

    if "identifier" not in http_request.params:
        raise ValueError("Question ID is required to edit a question.")
