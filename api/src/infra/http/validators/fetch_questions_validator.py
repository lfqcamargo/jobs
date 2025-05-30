from pydantic import BaseModel, ValidationError
from src.infra.http.views.http_types.http_request import HttpRequest
from ..middlewares.error_types.http_validation_param import HttpValidationParamError


def fetch_questions_validator(http_request: HttpRequest) -> None:
    """
    Validates the parameters in the given HTTP request for fetching questions.

    Args:
        http_request (HttpRequest): The HTTP request containing the parameters.

    Raises:
        ValidationError: If the validation fails for any of the fields.
    """

    class ParamData(BaseModel):
        """
        Validate Param Schema for Fetch Questions
        """

        user_id: int
        company_id: int

    try:
        ParamData(**http_request.params)
    except ValidationError as error:
        raise HttpValidationParamError(
            "Required parameters: user_id and company_id"
        ) from error
