"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_restx_demo.config import get_config

cors = CORS()
db = SQLAlchemy()

def create_app():
    app = Flask( 'flask-restx-demo' )

    app.config.from_object( get_config() )

    from flask_restx_demo.api import api_bp

    app.register_blueprint( api_bp )
	
    cors.init_app( app )

    db.init_app( app )
    with app.app_context():
        db.create_all()

    return app