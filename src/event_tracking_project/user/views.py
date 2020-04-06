from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from .forms import LoginForm, RegistrationForm
from .model import Users
from ..db import db

user_blueprint = Blueprint(name='user', import_name=__name__, url_prefix='/users')


@user_blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@user_blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter(Users.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы успешно зашли на сайт')
            return redirect(url_for('index'))
    flash('Неправильные имя или пароль')
    return redirect(url_for('users.login'))


@user_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))


@user_blueprint.route('/reg')
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Регистарция'
    form = RegistrationForm()
    return render_template('reg.html', page_title=title, form=form)


@user_blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = Users(username=form.username.data, email=form.email.data, city=form.city.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.reg'))
