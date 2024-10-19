# app/models/StationOperatorRecord.py
from .. import db

class StationOperatorRecord(db.Model):
    __tablename__ = 'StationOperatorRecord'
    id = db.Column(db.Integer, primary_key=True)
    operator_id = db.Column(db.Integer, db.ForeignKey('Operater.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('Station.id'))

    def __repr__(self):
        return f"<StationOperatorRecord(id={self.id}, operator_id={self.operator_id}, station_id={self.station_id})>"

    def to_dict(self):
        return {
            'id': self.id,
            'operator_id': self.operator_id,
            'station_id': self.station_id
        }