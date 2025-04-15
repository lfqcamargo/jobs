from flask import Blueprint, jsonify, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from src.infra.http.composers.create_skill_composer import create_skill_composer
from src.infra.http.composers.delete_skill_composer import delete_skill_composer
from src.infra.http.composers.edit_skill_composer import edit_skill_composer
from src.infra.http.composers.fetch_skills_composer import fetch_skills_composer

skill_route_bp = Blueprint("skills_routes", __name__)


@skill_route_bp.route("/users/<int:user_id>/skills", methods=["POST"])
def create_skill(user_id: int) -> tuple[HttpResponse, any]:
    """
    Create a new skill.

    This endpoint receives a JSON payload containing the skill data
    and persists it to the database.

    Returns:
        tuple[Response, any]: JSON response with a success or failure message and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(params={"user_id": user_id}, body=body)
    view = create_skill_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@skill_route_bp.route("/skills/<int:identifier>", methods=["DELETE"])
def delete_skill(identifier: int) -> tuple[HttpResponse, any]:
    """
    Delete a skill by its ID.

    This endpoint removes a skill from the database using its identifier.

    Args:
        identifier (int): Unique identifier of the skill to delete.

    Returns:
        tuple[Response, any]: JSON response indicating success or failure, with HTTP status code.
    """
    http_request = HttpRequest(params={"identifier": identifier})
    view = delete_skill_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@skill_route_bp.route("/skills/<int:identifier>", methods=["PUT"])
def edit_skill(identifier: int) -> tuple[HttpResponse, any]:
    """
    Edit an existing skill.

    This endpoint updates the information of a skill using its identifier.

    Args:
        identifier (int): Unique identifier of the skill to update.

    Request Body:
        JSON payload with the updated skill data.

    Returns:
        tuple[HttpResponse, any]: JSON response with updated data or error
        details, and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(params={"identifier": identifier}, body=body)
    view = edit_skill_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@skill_route_bp.route("/users/<int:user_id>/skills", methods=["GET"])
def fetch_skills(user_id: int) -> tuple[HttpResponse, any]:
    """
    Fetch all skills for a specific user.

    This endpoint retrieves all skills associated with a given user ID.

    Args:
        user_id (int): Unique identifier of the user whose skills should be retrieved.

    Returns:
        tuple[HttpResponse, any]: JSON response with a list of skills and HTTP status code.
    """
    http_request = HttpRequest(params={"user_id": user_id})
    view = fetch_skills_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
