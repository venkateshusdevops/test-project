from flask import Flask
from flask_pymongo import PyMongo
from config import AppConfig  # Import your application-specific configuration

# Create a Flask app instance
app = Flask(__name__)

# Load the application-specific configuration
app.config.from_object(AppConfig)

# Initialize PyMongo for MongoDB
mongo = PyMongo(app)

# Import your routes
from app import routes
