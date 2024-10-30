from .. import db

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)  # Added email column
    passwrd = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Login(id={self.id}, name={self.name}, email={self.email}, role={self.role})>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,  # Include email in the dictionary representation
            'passwrd': self.passwrd,
            'role': self.role
        }
