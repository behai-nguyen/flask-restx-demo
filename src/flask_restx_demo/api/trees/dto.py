"""Parsers and serializers for /trees API endpoints."""
import re

from flask_restx import Model
from flask_restx.fields import String
from flask_restx.inputs import URL
from flask_restx.reqparse import RequestParser

def tree_name( name ):
    """Validation method for a string containing only letters, '-' and space."""
    if not re.compile(r"^[A-Za-z, ' ', -]+$").match(name):
        raise ValueError(
            f"'{name}' contains one or more invalid characters. Tree name must "
            "contain only letters, hyphen and space characters."
        )
    return name

create_tree_reqparser = RequestParser( bundle_errors=True )
create_tree_reqparser.add_argument(
    'scientific_name',
    type=tree_name,
    location='form',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_tree_reqparser.add_argument(
    'common_name',
    type=tree_name,
    location='form',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_tree_reqparser.add_argument(
    'wiki_url',
    type=URL( schemes=[ 'http', 'https' ] ),
    location='form',
    required=True,
    nullable=False,
)

update_tree_reqparser = create_tree_reqparser.copy()
update_tree_reqparser.remove_argument( 'scientific_name' )

tree_model = Model( 'Tree', {
    'scientific_name': String,
    'common_name': String,
    'wiki_url': String,
})