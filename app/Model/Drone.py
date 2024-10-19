# app/models/Drone.py
from .. import db

class Drone(db.Model):
    __tablename__ = 'Drone'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ceiling = db.Column(db.Numeric(10, 2), nullable=False)
    speed = db.Column(db.Numeric(10, 2), nullable=False)
    battery = db.Column(db.Numeric(10, 2), nullable=False)
    payload = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Drone(id={self.id}, name={self.name}, ceiling={self.ceiling}, speed={self.speed})>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ceiling': str(self.ceiling),
            'speed': str(self.speed),
            'battery': str(self.battery),
            'payload': str(self.payload)
        }