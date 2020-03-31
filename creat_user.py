from getpass import getpass

from flask import Flask

from src.event_tracking_project import create_app
from event_tracking_project.user.model import db, Users


def create_user(app: Flask, user_name: str, password: str) -> str:
    with app.app_context():
        if Users.query.filter(Users.user_name == user_name).count():
            return 'Пользователь с таким именем уже сущесвтует'

        new_user = Users(username=user_name)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return 'Создан пользователь с id={}'.format(new_user.id)


if __name__ == '__main__':
    init_app = create_app()
    username = input('Введите имя:')
    password1 = getpass('Введите пароль:')
    password2 = getpass('Повторите пароль:')

    if not password1 == password2:
        print(create_user(init_app, username, password1))
    else:
        print()