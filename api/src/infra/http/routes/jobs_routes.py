from typing import Any
from flask import Blueprint, jsonify, Response, request
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.composers.run_linkedin_composer import run_linkedin_composer

job_route_bp = Blueprint("jobs_routes", __name__)


@job_route_bp.route("/jobs", methods=["POST"])
def run_linkedin() -> tuple[Response, Any]:
    """
    Endpoint to trigger LinkedIn automation tasks.

    This function acts as a Flask route handler for initiating LinkedIn automation tasks.
    It initializes an HTTP request and processes it using the RunLinkedinView. The result is
    then returned in the form of an HTTP response.

    The response contains details of the tasks performed, such as fetching company information
    or updating the LinkedIn profile.

    Returns:
        tuple[Response, Any]: A tuple containing the formatted JSON response and HTTP status code.
    """

    email = request.args.get("email")

    http_request = HttpRequest(params={"email": email})
    view = run_linkedin_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
