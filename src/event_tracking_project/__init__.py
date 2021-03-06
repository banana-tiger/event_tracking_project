from flask import Flask, render_template
from flask_login import LoginManager, login_required
from sqlalchemy import or_

from .config import PATH_TO_DB_MIGRATIONS
from .db import db

from .lastfm_crawler.model import Event
from .user.model import Users
from .user.views import user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')
    def index():
        title = 'EVENT'
        list_event = reversed(Event.query.filter(Event.city == 'Moscow').order_by(Event.event_date.desc())[-9:])
        return render_template('start_page.html', page_title=title, list_event=list_event)

    @app.route('/admin')
    @login_required
    def admin_index():
        return 'Привет админ!'

    return app
