from flask import Flask

from .database import init_db, db_session
from config import configure_app
from .route import user_route


def create_app():
    app = Flask(__name__)

    configure_app(app)

    init_db(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    app.register_blueprint(user_route, url_prefix='/api/v1')

    return app
