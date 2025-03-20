import logging
from flask import Flask
from flask_cors import CORS
from src.infra.database.postgres.settings.connection import db_connection_handler
from src.infra.http.routes.company_routes import company_route_bp
from src.infra.http.routes.jobs_routes import job_route_bp
from src.infra.http.routes.user_routes import user_route_bp
from src.infra.scripts.init_data_database import init_data_database
from src.infra.http.middlewares.error_middleware import error_middleware


def create_app() -> Flask:
    """
    Init App
    """
    db_connection_handler.connect_to_db()
    init_data_database(db_connection_handler)

    app = Flask(__name__)
    CORS(app)

    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(company_route_bp)
    app.register_blueprint(job_route_bp)
    app.register_blueprint(user_route_bp)

    @app.errorhandler(Exception)
    def middleware_error(error) -> any:
        return error_middleware(error)

    return app
