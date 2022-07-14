"""API endpoint definitions for /trees namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource

from flask_restx_demo.api.trees.dto import (
    create_tree_reqparser,
    tree_model,
)

from flask_restx_demo.api.trees.bro import (
    create_tree,
    retrieve_tree_list,
)

tree_ns = Namespace( name="trees", validate=True )
# tree_ns.models[ tree_model.name ] = tree_model
# tree_ns.add_model( tree_model.name, tree_model )
tree_ns.model( tree_model.name, tree_model )

@tree_ns.route( "", endpoint='tree_list' )
@tree_ns.response( int(HTTPStatus.BAD_REQUEST), 'Validation error.' )
@tree_ns.response( int(HTTPStatus.INTERNAL_SERVER_ERROR), 'Internal server error.' )
class TreeList( Resource ):
    """ Handles HTTP requests to URL: /trees. """

    @tree_ns.response( int(HTTPStatus.OK), 'Retrieved tree list.' )
    def get( self ):
        """ Retrieve tree list. """
        return retrieve_tree_list()

    @tree_ns.response(int(HTTPStatus.CREATED), 'Added new tree.' )
    @tree_ns.response(int(HTTPStatus.CONFLICT), 'Tree name already exists.' )
    @tree_ns.expect( create_tree_reqparser )
    def post( self ):
        """ Create a tree. """
        tree_dict = create_tree_reqparser.parse_args()
        return create_tree( tree_dict )
