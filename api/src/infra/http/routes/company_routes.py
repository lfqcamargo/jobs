from typing import Any
from flask import Blueprint, jsonify, Response
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.composers.fetch_companies_composer import fetch_companies_composer

company_route_bp = Blueprint("companies_routes", __name__)


@company_route_bp.route("/companies", methods=["GET"])
def fetch_companies() -> tuple[Response, Any]:
    """
    Endpoint to fetch a list of companies.

    This function acts as a Flask route handler for fetching companies. It initializes
    an HTTP request, processes it using the FetchCompaniesView, and returns a formatted
    HTTP response.

    Returns:
        tuple[Response, Any]: A tuple containing the JSON response and HTTP status code.
    """
    http_request = HttpRequest()
    view = fetch_companies_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
