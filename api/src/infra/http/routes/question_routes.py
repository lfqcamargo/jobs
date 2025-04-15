from flask import Blueprint, jsonify, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from src.infra.http.composers.create_question_composer import create_question_composer
from src.infra.http.composers.delete_question_composer import delete_question_composer
from src.infra.http.composers.edit_question_composer import edit_question_composer
from src.infra.http.composers.fetch_questions_composer import fetch_questions_composer

question_route_bp = Blueprint("questions_routes", __name__)


@question_route_bp.route(
    "/users/<int:user_id>/company/<int:company_id>/questions", methods=["POST"]
)
def create_question(user_id: int, company_id: int) -> tuple[HttpResponse, any]:
    """
    Create a new question.

    This endpoint receives a JSON payload containing the question data
    and persists it to the database.

    Returns:
        tuple[Response, any]: JSON response with a success or failure message and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(
        params={"user_id": user_id, "company_id": company_id}, body=body
    )
    view = create_question_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@question_route_bp.route("/questions/<int:identifier>", methods=["DELETE"])
def delete_question(identifier: int) -> tuple[HttpResponse, any]:
    """
    Delete a question by its ID.

    This endpoint removes a question from the database using its identifier.

    Args:
        identifier (int): Unique identifier of the question to delete.

    Returns:
        tuple[Response, any]: JSON response indicating success or failure, with HTTP status code.
    """
    http_request = HttpRequest(params={"identifier": identifier})
    view = delete_question_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@question_route_bp.route("/questions/<int:identifier>", methods=["PUT"])
def edit_question(identifier: int) -> tuple[HttpResponse, any]:
    """
    Edit an existing question.

    This endpoint updates the information of a question using its identifier.

    Args:
        identifier (int): Unique identifier of the question to update.

    Request Body:
        JSON payload with the updated question data.

    Returns:
        tuple[HttpResponse, any]: JSON response with updated data or error
        details, and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(params={"identifier": identifier}, body=body)
    view = edit_question_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@question_route_bp.route(
    "/users/<int:user_id>/company/<int:company_id>/questions", methods=["GET"]
)
def fetch_questions(user_id: int, company_id: int) -> tuple[HttpResponse, any]:
    """
    Fetch all questions for a specific user.

    This endpoint retrieves all questions associated with a given user ID.

    Args:
        user_id (int): Unique identifier of the user whose questions should be retrieved.
        company_id (int): Unique identifier of the company whose questions should be retrieved.

    Returns:
        tuple[HttpResponse, any]: JSON response with a list of questions and HTTP status code.
    """
    http_request = HttpRequest(params={"user_id": user_id, "company_id": company_id})
    view = fetch_questions_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
