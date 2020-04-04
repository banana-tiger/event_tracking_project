import os
from pathlib import Path

THIS_DIR = Path(__file__).absolute().parent

PATH_TO_DB_DIR = THIS_DIR.parent.parent / 'db'
PATH_TO_DB_DATA = PATH_TO_DB_DIR / 'data/db.sqlite'
PATH_TO_DB_MIGRATIONS = PATH_TO_DB_DIR / 'migrations'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(PATH_TO_DB_DATA)

SECRET_KEY = os.getenv('EVENT_TRACKING_SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False
