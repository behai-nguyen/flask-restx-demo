""" Flask-RESTX API blueprint configuration. """
from flask import Blueprint
from flask_restx import Api

from flask_restx_demo.api.trees.routes import tree_ns

api_bp = Blueprint( 'api', __name__, url_prefix='/api/v1' )

api = Api(
    api_bp,
    version='1.0',
    title='Flask-RESTX API Demo',
    description='Welcome to Flask-RESTX API with Swagger UI documentation',
    doc='/ui',
)

api.add_namespace( tree_ns, path='/trees' )
