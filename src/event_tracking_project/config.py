import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
SECRET_KEY = 'iuah45als8j2rjc8j59dj20dj3irjqcbqr4'
