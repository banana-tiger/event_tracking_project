from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    country_code = db.Column(db.String, unique=True, nullable=False)
    flightable = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Airports {} {} {}>'.format(self.country_code, self.name, self.code)