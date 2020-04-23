from ..db import db


class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, nullable=False)
    flightable = db.Column(db.Boolean, nullable=False)
    codes_combo = db.Column(db.String, nullable=False, index=True)


# некоторые города обладают одинаковым названием поэтому есть идея сделать комбинированное поле code + country_code
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, nullable=False)
    codes_combo = db.Column(db.String, nullable=False, index=True)
