from pathlib import Path

from flask import Flask

from flask_migrate import Migrate

from src.event_tracking_project.config import PATH_TO_DB_MIGRATIONS
from src.event_tracking_project.db import db

from src.event_tracking_project.aviasales_repo import models
from src.event_tracking_project.user.model import Users, Artists, Subscription

from src.event_tracking_project.lastfm_crawler.model import Event

THIS_DIR = Path(__file__).resolve().parent


def create_app():
    app = Flask(__name__)
    config_path = THIS_DIR / "src" / "event_tracking_project" / "config.py"
    app.config.from_pyfile(config_path)
    db.init_app(app)
    migrate = Migrate(app, db, directory=PATH_TO_DB_MIGRATIONS)

    return app
