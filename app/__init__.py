from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize the database object
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Load the configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    # File upload configurations
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB upload limit
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Define the upload folder path
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Initialize the database and migration objects
    db.init_app(app)
    Migrate(app, db)

    # Import and register the routes (blueprint)
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
