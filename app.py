# app.py
from app import create_app
from flask_migrate import Migrate
from app import db  # Importing the db object from app/__init__.py

# Create the app using the factory function
app = create_app()

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
