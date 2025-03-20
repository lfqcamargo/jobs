from typing import Any
from flask import Blueprint, jsonify, Response, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.composers.create_user_composer import create_user_composer

user_route_bp = Blueprint("users_routes", __name__)


@user_route_bp.route("/users", methods=["POST"])
def run_linkedin() -> tuple[Response, Any]:
    """
    Endpoint to create a new user.

    This function acts as a Flask route handler for user creation requests.
    It initializes an HTTP request, processes it using the CreateUserView, and returns
    the formatted HTTP response.

    Returns:
        tuple[Response, Any]: A tuple containing the formatted JSON response and HTTP status code.
    """

    body = request.json
    http_request = HttpRequest(body=body)
    view = create_user_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
