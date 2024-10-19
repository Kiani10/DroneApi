# app/models/Operater.py
from .. import db

class Operater(db.Model):
    __tablename__ = 'Operater'
    id = db.Column(db.Integer, db.ForeignKey('Login.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    shift = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Operater(id={self.id}, name={self.name}, shift={self.shift})>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'shift': self.shift
        }