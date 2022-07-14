"""Class definition for Tree model."""

from flask_restx_demo import db

class Tree( db.Model ):
    """Tree model for a generic resource for Flask-RESTX API Demo."""

    __tablename__ = "tree"

    id = db.Column( db.Integer, primary_key=True, autoincrement=True )
    scientific_name = db.Column( db.String(128), unique=True, nullable=False )
    common_name = db.Column( db.String(128), nullable=False )
    wiki_url = db.Column( db.String(255), nullable=False )

    def __repr__(self):
        return f"<Tree scientific name={self.scientific_name}, common name={self.common_name}>"

    @classmethod
    def find_by_scientific_name( cls, scientific_name ):
        return cls.query.filter_by( scientific_name=scientific_name ).first()
