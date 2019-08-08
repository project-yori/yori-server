from flask import jsonify
from flask_restplus import Namespace, Resource, fields

api = Namespace('photo', description='Photos related operations')

photo = api.model('photo', {
    'photo_group': fields.String(required=True, description='グループ'),
    'photo_member': fields.String(required=True, description='名前'),
    'photo_costume': fields.String(required=True, description='服'),
    'photo_type': fields.String(required=True, description='距離'),
    'photo_number': fields.Integer(required=True, description='数'),
    'photo_folder': fields.String(required=True, description='フォルダ')
})

PHOTOS = [
    {
        "photo_group": "乃木坂46",
        "photo_member": "樋口日奈",
        "photo_costume": "2019 summer concert 1",
        "photo_type": "ヨリ",
        "photo_number": 1,
        "photo_folder": "all"
    }
]

@api.route('/')
class MemberList(Resource):
    @api.doc('get_photos')
    @api.marshal_list_with(photo)
    def get(self):
        return PHOTOS
