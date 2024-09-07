import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    UPLOAD_FOLDER = 'app/static/uploads'  # Secure upload directory
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB upload limit for photos
