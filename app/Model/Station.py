# app/models/Station.py
from .. import db

class Station(db.Model):
    __tablename__ = 'Station'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    location_pad_img = db.Column(db.Text)

    def __repr__(self):
        return f"<Station(id={self.id}, name={self.name}, location={self.location})>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'location_pad_img': self.location_pad_img
        }