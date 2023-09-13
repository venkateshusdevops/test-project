import os
from flask import Flask
from flask_pymongo import PyMongo

# Initialize Flask app
app = Flask(__name__)

# Load the configuration based on the environment
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.dev_config.DevConfig')
elif os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config.prod_config.ProdConfig')
else:
    app.config.from_object('config.default_config.DefaultConfig')

# Initialize PyMongo for MongoDB
mongo = PyMongo(app)

# Import routes
from app import routes
