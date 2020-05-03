from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from .forms import DeletedSubscriptionForm, LoginForm, RegistrationForm, SubscriptionForm, EventForm
from .model import Users, Artists, Subscription
from ..lastfm_crawler.model import Event
from ..lastfm_crawler.get_all_event import get_events_by_artist
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
    title = 'Регистрация'
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


@user_blueprint.route('/subscription')
def subscription():

    title = 'Подписки'
    form = SubscriptionForm()
    list_sub = Subscription.query.filter_by(user_id=current_user.id)
    return render_template('profile/subscription.html', page_title=title, form=form, list_sub=list_sub)


@user_blueprint.route('/subs-create', methods=['POST'])
@login_required
def create_sub():
    form = SubscriptionForm()
    if form.validate_on_submit():
        artist = Artists.get_or_create(db.session, form.artist_name.data)

        sub = Subscription(artist_id=artist.artist_id, user_id=current_user.id)
        db.session.add(sub)
        db.session.commit()

        return redirect(url_for('user.subscription'))
    return redirect(url_for('user.subscription'))


@user_blueprint.route('/subs-del/<int:subs_id>', methods=['POST'])
@login_required
def delete_sub(subs_id):
    form = DeletedSubscriptionForm()
    sub = Subscription.query.filter_by(subs_id=subs_id).first()

    db.session.delete(sub)
    db.session.commit()
    return redirect(url_for('user.subscription'))


@user_blueprint.route('/profile')
def profile():
    title = 'Профиль'
    form = RegistrationForm()
    user = Users.query.filter_by(id=current_user.id).first()
    return render_template('profile/profile.html', page_title=title, user=user)


@user_blueprint.route('/events/<int:subs_artist_id>')
def events(subs_artist_id):
    form = EventForm()
    page_title = 'Мероприятия'
    list_events = Event.query.filter_by(artist_id=subs_artist_id).all()
    if not list_events:
        artist = Artists.query.filter_by(artist_id=subs_artist_id).first()
        get_events_by_artist(artist)
        list_events = Event.query.filter_by(artist_id=subs_artist_id).all()

    return render_template('event/events.html', page_title=page_title, list_events=list_events)
