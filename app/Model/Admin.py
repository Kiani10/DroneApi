# app/models/Admin.py
from .. import db

class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, db.ForeignKey('Login.id'), primary_key=True)
    department = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"<Admin(id={self.id}, department={self.department})>"

    def to_dict(self):
        return {
            'id': self.id,
            'department': self.department
        }
