from pydantic import BaseModel, ValidationError, EmailStr
from src.infra.http.views.http_types.http_request import HttpRequest
from ..middlewares.error_types.http_validation_param import HttpValidationParamError


def validate_request_params(http_request: HttpRequest) -> None:
    """
    Validates the parameters in the given HTTP request.

    Args:
        http_request (HttpRequest): The HTTP request containing the parameters.

    Raises:
        ValidationError: If the validation fails for any of the fields.
    """

    class ParamData(BaseModel):
        """
        Validate Param Schema
        """

        email: EmailStr

    try:
        ParamData(**http_request.param)
    except ValidationError as error:
        raise HttpValidationParamError("required parameters: email") from error
