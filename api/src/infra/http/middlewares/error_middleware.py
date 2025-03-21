from flask import jsonify
from pydantic import ValidationError
from .error_types.http_validation_param import HttpValidationParamError
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.errors.wrong_credentials import WrongCredentialsError
from src.infra.http.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_conflict_request import HttpConficlitError
from .error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def error_middleware(error: Exception) -> HttpResponse:
    """
    Handles exceptions and maps them to appropriate HTTP responses.

    Args:
        error (Exception): The exception to handle.

    Returns:
        HttpResponse: The HTTP response corresponding to the handled exception.
    """

    if isinstance(error, AlreadyExistsError):
        response = HttpResponse(
            status_code=409,
            body={"errors": [error.to_dict()]},
        )
        return jsonify(response.body), response.status_code

    if isinstance(error, ResourNotFoundError):
        response = HttpResponse(
            status_code=404,
            body={"errors": [error.to_dict()]},
        )
        return jsonify(response.body), response.status_code

    if isinstance(error, WrongCredentialsError):
        response = HttpResponse(
            status_code=404,
            body={"errors": [error.to_dict()]},
        )
        return jsonify(response.body), response.status_code

    if isinstance(error, ValidationError):
        response = HttpResponse(
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
        return jsonify(response.body), response.status_code

    if isinstance(error, HttpValidationParamError):
        response = HttpResponse(
            status_code=error.status_code,
            body={"errors": error.message},
        )
        return jsonify(response.body), response.status_code

    if isinstance(
        error,
        (
            HttpBadRequestError,
            HttpNotFoundError,
            HttpUnprocessableEntityError,
            HttpConficlitError,
        ),
    ):
        response = HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )
        return jsonify(response.body), response.status_code

    # Fallback for generic exceptions
    response = HttpResponse(
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
    return jsonify(response.body), response.status_code
