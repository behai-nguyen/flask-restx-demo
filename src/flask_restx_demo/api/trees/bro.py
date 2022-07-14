"""Business rules ( logic ) for /trees API endpoints."""
from http import HTTPStatus

from flask import jsonify
from flask_restx import abort, marshal

from flask_restx_demo import db
from flask_restx_demo.models.tree import Tree
from flask_restx_demo.api.trees.dto import tree_model

def _create_successful_response( status_code, message ):
    response = jsonify(
        status="success",
        message=message,
    )
    response.status_code = status_code
    response.headers[ 'Cache-Control' ] = 'no-store'
    response.headers[ 'Pragma' ] = 'no-cache'
    return response

def create_tree( tree_dict ):
    if Tree.find_by_scientific_name( tree_dict['scientific_name'] ):
        abort( HTTPStatus.CONFLICT, f"{tree_dict['scientific_name']} is already entered", status="fail" )
    new_tree = Tree( **tree_dict )
    db.session.add( new_tree )
    db.session.commit()
    return _create_successful_response(
        status_code=HTTPStatus.CREATED,
        message='successfully created',
    )

def retrieve_tree_list():
    data = Tree.query.all()
    response_data = marshal( data, tree_model )
    response = jsonify( response_data )
    return response
