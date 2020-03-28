# для запуска из cmd
# set FLASK_APP=src\event_tracking_project && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from event_tracking_project.model import db, Users
from event_tracking_project.forms import LoginForm



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'


    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')
    def index():
        title = 'EVENT'
        return render_template('start_page.html', page_title=title)


    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    
    @app.route('/proess-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        
        if form.validate_on_submit():
            user = Users.query.filter(Users.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно зашли на сайт')
                return redirect(url_for('index'))
        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))


    @app.route('/loguot')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        return 'Привет админ!'

    return app
