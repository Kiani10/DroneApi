# app/models/MissionCoordinates.py
from .. import db

class MissionCoordinates(db.Model):
    __tablename__ = 'MissionCoordinates'
    id = db.Column(db.Integer, primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey('Mission.id', ondelete="CASCADE"), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<MissionCoordinates(id={self.id}, latitude={self.latitude}, longitude={self.longitude})>"

    def to_dict(self):
        return {
            'id': self.id,
            'mission_id': self.mission_id,
            'latitude': self.latitude,
            'longitude': self.longitude
        }