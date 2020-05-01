from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    city = StringField('Город проживания', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')],
                              render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class SubscriptionForm(FlaskForm):
    artist_name = StringField('Группа', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('подписаться', render_kw={"class": "btn btn-primary"})


class DeletedSubscriptionForm(FlaskForm):
    submit = SubmitField(render_kw={"class": "btn btn-primary"})


class EventForm(FlaskForm):
    submit = SubmitField(render_kw={"class": "btn btn-primary"})

