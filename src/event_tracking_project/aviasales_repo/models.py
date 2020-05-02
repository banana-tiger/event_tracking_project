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
    de_name = db.Column(db.String, nullable=True)
    ru_name = db.Column(db.String, nullable=True)
    it_name = db.Column(db.String, nullable=True)
    es_name = db.Column(db.String, nullable=True)
    fr_name = db.Column(db.String, nullable=True)
    # Добавление ручных полей для модераторов (админов) для ручного исправления несостыковок названий городов между
    # LastFM и aviasales
    moderated_name1 = db.Column(db.String, nullable=True)
    moderated_name2 = db.Column(db.String, nullable=True)

    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, db.ForeignKey('countries.country_code'), nullable=False)
    codes_combo = db.Column(db.String, nullable=False, index=True)


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # Добавление ручных полей для модераторов (админов) для ручного исправления несостыковок названий стран между
    # LastFM и aviasales
    moderated_name = db.Column(db.String, nullable=True)

    country_code = db.Column(db.String, unique=True, nullable=False)
    cities = db.relationship('City', backref='countries', lazy=True)


class Airline(db.Model):
    __tablename__ = 'airlines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    airline_code = db.Column(db.String, nullable=True)


class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String, nullable=False)
    airline_code = db.Column(db.String, nullable=False)
    flight_number = db.Column(db.String, nullable=False)
    departure_at = db.Column(db.DateTime, nullable=False)
    return_at = db.Column(db.DateTime, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
