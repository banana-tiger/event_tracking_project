from flask import Flask

from flask_migrate import Migrate

from src.event_tracking_project.config import PATH_TO_DB_MIGRATIONS
from src.event_tracking_project.db import db

from src.event_tracking_project.aviasales_repo.models import Airports, Cities
from src.event_tracking_project.user.model import Users


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('src\event_tracking_project\config.py')
    db.init_app(app)
    migrate = Migrate(app, db, directory=PATH_TO_DB_MIGRATIONS)

    return app
