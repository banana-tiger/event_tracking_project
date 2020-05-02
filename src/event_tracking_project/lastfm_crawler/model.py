from ..db import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.DateTime)
    title = db.Column(db.Text)
    place = db.Column(db.Text)
    city = db.Column(db.Text)
    country = db.Column(db.Text)
    status = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"))


    def exists_in_db(self) -> bool:
        event_exists = Event.query.filter(Event.event_date == self.event_date,
                                          Event.place == self.place,
                                          Event.title == self.title,
                                          Event.artist_id == self.artist_id).count()
        return event_exists > 0
