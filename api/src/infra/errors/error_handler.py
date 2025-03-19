from pydantic import ValidationError
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.wrong_credentials import WrongCredentialsError
from src.infra.http.views.http_types.http_response import HttpResponse
from src.infra.errors.error_types.http_bad_request import HttpBadRequestError
from src.infra.errors.error_types.http_not_found import HttpNotFoundError
from src.infra.errors.error_types.http_conflict_request import HttpConficlitError
from src.infra.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def handle_errors(error: Exception) -> HttpResponse:
    """
    Handles exceptions and maps them to appropriate HTTP responses.

    Args:
        error (Exception): The exception to handle.

    Returns:
        HttpResponse: The HTTP response corresponding to the handled exception.
    """

    if isinstance(error, AlreadyExistsError):
        return HttpResponse(
            status_code=409,
            body={"errors": [error.to_dict()]},
        )

    if isinstance(error, ResourNotFoundError):
        return HttpResponse(
            status_code=404,
            body={"errors": [error.to_dict()]},
        )

    if isinstance(error, WrongCredentialsError):
        return HttpResponse(
            status_code=404,
            body={"errors": [error.to_dict()]},
        )

    if isinstance(error, ValidationError):
        return HttpResponse(
            status_code=422,
            body={
                "errors": [
                    {
                        "title": "Validation Error",
                        "detail": e["msg"],
                        "field": e.get("loc"),
                    }
                    for e in error.errors()
                ]
            },
        )

    if isinstance(
        error,
        (
            HttpBadRequestError,
            HttpNotFoundError,
            HttpUnprocessableEntityError,
            HttpConficlitError,
        ),
    ):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    # Fallback for generic exceptions
    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "title": "Server Error",
                    "detail": (
                        str(error) if isinstance(error, Exception) else repr(error)
                    ),
                }
            ]
        },
    )
