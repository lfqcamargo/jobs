import logging
from flask import Flask
from flask_cors import CORS
from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.http.routes.company_routes import company_route_bp


def create_app() -> Flask:
    """
    Init App
    """
    db_connection_handler.connect_to_db()

    app = Flask(__name__)
    CORS(app)

    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(company_route_bp)

    return app
