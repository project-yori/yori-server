from flask_restplus import Api
from .photo import api as photo
from .member import api as member

api = Api(
    title='Yori API',
    version='1.0',
    description='API Documentation',
    # All API metadatas
)

api.add_namespace(photo)
api.add_namespace(member)
