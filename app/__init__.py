from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Import routes
    from .routes import main
    app.register_blueprint(main)
    
    return app
