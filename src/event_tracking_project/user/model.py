from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..db import db


class Users(db.Model, UserMixin):
    __table_name__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text)
    subscriptions = db.relationship('Subscription', backref='users', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User name {} id={}>'.format(self.username, self.id)


class Artists(db.Model):
    __table_name__ = "artists"
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(255), nullable=False)
    subscriptions = db.relationship('Subscription', backref='artists', lazy=True)


    @classmethod
    def get_or_create(cls, session, artist_name: str):
        print(artist_name)
        artist = cls.query.filter_by(artist_name=artist_name).first()
        if not artist:
            artist = cls(artist_name=artist_name)
            session.add(artist)
            session.commit()

        return artist


class Subscription(db.Model):
    subs_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    artist = db.relationship('Artists', backref='subscription')
