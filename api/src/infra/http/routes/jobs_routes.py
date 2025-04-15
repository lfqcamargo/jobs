from flask import Blueprint, jsonify, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse
from src.infra.http.composers.run_linkedin_composer import run_linkedin_composer


jobs_route_bp = Blueprint("jobs_routes", __name__)


@jobs_route_bp.route("/jobs/linkedin/users/<user_id>", methods=["POST"])
def execute_job(user_id: int) -> tuple[HttpResponse, any]:
    """
    Endpoint to Run Linkedin.

    This function acts as a Flask route handler for user Run Linkedin.
    It initializes an HTTP request, processes it using the Run LinkedinView, and returns
    the formatted HTTP response.

    Returns:
        tuple[Response, Any]: A tuple containing the formatted JSON response and HTTP status code.
    """
    body = request.get_json()
    http_request = HttpRequest(params={"user_id": user_id}, body=body)
    view = run_linkedin_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
