from getpass import getpass
import sys

from src.event_tracking_project import create_app
from src.event_tracking_project.model import db, Users

app = create_app()
with app.app_context():
    username = input('Введите имя:')

    if Users.query.filter(Users.username == username).count():
        print('Пользователь с таким именем уже сущесвтует')
        sys.exit(0)

    password1 = getpass('Введите пароль:')
    password2 = getpass('Повторите пароль:')
    
    if not password1 == password2:
        print('Пароли не совпадают')
        sys.exit(0) 

    new_user = Users(username=username)
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))