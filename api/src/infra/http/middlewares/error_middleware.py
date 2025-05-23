from flask import jsonify
from pydantic import ValidationError
from src.core.errors.already_exists_error import AlreadyExistsError

# from src.core.errors.domain_error import DomainError
from src.core.errors.resource_not_found_error import ResourceNotFoundError

# from src.core.errors.wrong_credentials import WrongCredentialsError
from src.infra.http.views.http_types.http_response import HttpResponse
from .error_types.http_validation_param import HttpValidationParamError

# from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_conflict_request import HttpConficlitError

# from .error_types.http_unprocessable_entity import (
#     HttpUnprocessableEntityError,
# )


def error_middleware(error: Exception) -> HttpResponse:
    """
    Handles exceptions and maps them to appropriate HTTP responses.

    Args:
        error (Exception): The exception to handle.

    Returns:
        HttpResponse: The HTTP response corresponding to the handled exception.
    """
    if isinstance(error, ValueError):
        response = HttpResponse(
            status_code=422,
            body={"errors": [{"title": "Validation Error", "detail": str(error)}]},
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

    if isinstance(error, AlreadyExistsError):
        http = HttpConficlitError(error.message)
        response = HttpResponse(
            status_code=http.status_code,
            body={"errors": [{"title": http.name, "detail": http.message}]},
        )
        return jsonify(response.body), response.status_code

    if isinstance(error, ResourceNotFoundError):
        http = HttpNotFoundError(error.message)
        response = HttpResponse(
            status_code=http.status_code,
            body={"errors": [{"title": http.name, "detail": http.message}]},
        )
        return jsonify(response.body), response.status_code

    # if isinstance(
    #     error,
    #     (
    #         HttpBadRequestError,
    #         HttpUnprocessableEntityError,
    #
    #     ),
    # ):
    #     response = HttpResponse(
    #         status_code=error.status_code,
    #         body={"errors": [{"title": error.name, "detail": error.message}]},
    #     )
    #     return jsonify(response.body), response.status_code

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
