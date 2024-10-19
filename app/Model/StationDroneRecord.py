# app/models/StationDroneRecord.py
from .. import db

class StationDroneRecord(db.Model):
    __tablename__ = 'StationDroneRecord'
    id = db.Column(db.Integer, primary_key=True)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('Station.id'))

    def __repr__(self):
        return f"<StationDroneRecord(id={self.id}, drone_id={self.drone_id}, station_id={self.station_id})>"

    def to_dict(self):
        return {
            'id': self.id,
            'drone_id': self.drone_id,
            'station_id': self.station_id
        }