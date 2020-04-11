from ..db import db


class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, nullable=False)
    flightable = db.Column(db.Boolean, nullable=False)
    codes_combo = db.Column(db.String, nullable=False, index=True)


# некоторые города обладают одинаковым названием поэтому есть идея сделать комбинированное поле code + country_code
class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, nullable=False)
    codes_combo = db.Column(db.String, nullable=False, index=True)
