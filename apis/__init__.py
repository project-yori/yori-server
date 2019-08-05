from flask_restplus import Api
from .cat import api as cat

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cat)
