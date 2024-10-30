# app/controllers/UserController.py
from ..Model.Login import Login
from ..Model.Admin import Admin
from ..Model.Operater import Operater
from .. import db

class UserController:
    # Login (General User) Functions
    @staticmethod
    def create_user(data):
        new_user = Login(
            name=data['name'], 
            email=data['email'],  # Added email
            passwrd=data['passwrd'], 
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return Login.query.get(user_id)

    @staticmethod
    def get_all_users():
        return Login.query.all()

    @staticmethod
    def update_user(user_id, data):
        user = Login.query.get(user_id)
        if user:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.passwrd = data.get('passwrd', user.passwrd)
            user.role = data.get('role', user.role)
            db.session.commit()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = Login.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    # Operator Functions
    @staticmethod
    def create_operator(data):
        # Step 1: Create a user in the Login table
        new_user = Login(
            name=data['name'],
            email=data['email'],
            passwrd=data['passwrd'],  # Assuming you're passing a password in the request
            role='operator'  # Hardcode role as 'operator' or dynamically set it//because we cannot create admin in this
        )
        db.session.add(new_user)
        db.session.commit()

        # Step 2: Create the operator in the Operator table with the same id from Login
        new_operator = Operater(
            id=new_user.id,  # Use the id from the newly created Login entry
            name=data['name'], 
            shift=data['shift']
        )
        db.session.add(new_operator)
        db.session.commit()

        return new_operator  # Return the created operator object

    @staticmethod
    def get_operator_by_id(operator_id):
        return Operater.query.get(operator_id)

    @staticmethod
    def get_all_operators():
        return Operater.query.all()

    @staticmethod
    def update_operator(operator_id, data):
        operator = Operater.query.get(operator_id)
        if operator:
            operator.name = data.get('name', operator.name)
            operator.shift = data.get('shift', operator.shift)
            db.session.commit()
            return operator
        return None

    @staticmethod
    def delete_operator(operator_id):
        operator = Operater.query.get(operator_id)
        if operator:
            db.session.delete(operator)
            db.session.commit()
            return True
        return False

    # Admin Functions
    @staticmethod
    def create_admin(data):
        new_admin = Admin(
            id=data['id'], 
            department=data['department']
        )
        db.session.add(new_admin)
        db.session.commit()
        return new_admin

    @staticmethod
    def get_admin_by_id(admin_id):
        return Admin.query.get(admin_id)

    @staticmethod
    def get_all_admins():
        return Admin.query.all()

    @staticmethod
    def update_admin(admin_id, data):
        admin = Admin.query.get(admin_id)
        if admin:
            admin.department = data.get('department', admin.department)
            db.session.commit()
            return admin
        return None

    @staticmethod
    def delete_admin(admin_id):
        admin = Admin.query.get(admin_id)
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return True
        return False
