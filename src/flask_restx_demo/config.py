"""Flask app config settings."""
import os

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = os.getenv( 'SECRET_KEY' )
    FLASK_APP = os.getenv( 'FLASK_APP' )
    FLASK_ENV = os.getenv( 'FLASK_ENV' )
    SQLALCHEMY_DATABASE_URI = os.getenv( 'SQLALCHEMY_DATABASE_URI' )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv( 'SQLALCHEMY_TRACK_MODIFICATIONS' )

def get_config():
    """Retrieve environment configuration settings."""
    return Config