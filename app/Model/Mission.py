# app/models/Mission.py
from .. import db

class Mission(db.Model):
    __tablename__ = 'Mission'
    id = db.Column(db.Integer, primary_key=True)
    mission_datetime = db.Column(db.DateTime, nullable=False)
    location_pad = db.Column(db.String(255), nullable=False)
    img = db.Column(db.Text)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'))

    def __repr__(self):
        return f"<Mission(id={self.id}, mission_datetime={self.mission_datetime}, location_pad={self.location_pad})>"

    def to_dict(self):
        return {
            'id': self.id,
            'mission_datetime': self.mission_datetime,
            'location_pad': self.location_pad,
            'img': self.img,
            'drone_id': self.drone_id
        }