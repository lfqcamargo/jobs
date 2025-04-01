import json
from flask import Blueprint, jsonify, Response, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from src.infra.http.composers.create_user_composer import create_user_composer
from src.infra.http.composers.delete_user_composer import delete_user_composer
from src.infra.http.composers.edit_user_composer import edit_user_composer
from src.infra.http.composers.fetch_users_composer import fetch_users_composer


user_route_bp = Blueprint("users_routes", __name__)


@user_route_bp.route("/users", methods=["POST"])
def run_linkedin() -> tuple[Response, any]:
    """
    Endpoint to create a new user.

    This function acts as a Flask route handler for user creation requests.
    It initializes an HTTP request, processes it using the CreateUserView, and returns
    the formatted HTTP response.

    Returns:
        tuple[Response, Any]: A tuple containing the formatted JSON response and HTTP status code.
    """
    files = request.files.get("curriculum")
    body = json.loads(request.form.get("json_data"))
    http_request = HttpRequest(body=body, files=files)
    view = create_user_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id: int) -> tuple[Response, any]:
    """
    Endpoint to delete a user by ID.

    This function acts as a Flask route handler for user deletion requests.
    It initializes an HTTP request, processes it using the DeleteUserView, and returns
    the formatted HTTP response.

    Args:
        id (int): The ID of the user to be deleted.

    Returns:
        tuple[Response, Any]: A tuple containing the formatted JSON response and HTTP status code.
    """
    http_request = HttpRequest(params={"id": id})
    view = delete_user_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/users/<int:id>", methods=["PUT"])
def edit_user(id: int) -> tuple[HttpResponse, any]:
    """
    Endpoint to edit an existing user by ID.

    This function acts as a Flask route handler for user edit requests.
    It initializes an HTTP request, processes it using the EditUserView,
    and returns the formatted HTTP response.

    Args:
        id (int): The ID of the user to be edited.

    Returns:
        tuple[HttpResponse, any]: A tuple containing the formatted JSON
        response and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(body=body, params={"id": id})
    view = edit_user_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/users", methods=["GET"])
def fetch_users() -> tuple[HttpResponse, any]:
    """
    Endpoint to fetch all users.

    This function acts as a Flask route handler for fetching all users,
    without requiring an ID in the URL or body.

    Returns:
        tuple[HttpResponse, any]: A tuple containing the formatted JSON response
        and HTTP status code.
    """
    http_request = HttpRequest()
    view = fetch_users_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
