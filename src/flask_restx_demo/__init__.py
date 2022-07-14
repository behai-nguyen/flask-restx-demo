"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_restx_demo.config import get_config

db = SQLAlchemy()

def create_app():
    app = Flask( 'flask-restx-demo' )

    app.config.from_object( get_config() )

    from flask_restx_demo.api import api_bp

    app.register_blueprint( api_bp )

    db.init_app( app )
    with app.app_context():
        db.create_all()

    return app