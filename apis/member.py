from flask import jsonify
from flask_restplus import Namespace, Resource, fields

api = Namespace('member', description='Members related operations')

member = api.model('member', {
    'member_name_en': fields.String(required=True, description='英語'),
    'member_name': fields.String(required=True, description='名前'),
    'member_name_gana': fields.String(required=True, description='ひらがな'),
    'member_gen': fields.Integer(required=True, description='期'),
    'member_graduated': fields.Boolean(required=True, description='卒業'),
    'group_id': fields.String(required=True, description='group id')
})

MEMBERS = [
    {
        'member_name_en': 'imaizumi_yui',
        'member_name': '今泉佑唯',
        'member_name_gana': 'いまいずみ_ゆい',
        'member_gen': 1,
        'member_graduated': True,
        'group_id': 'keyakizaka'
    }
]

@api.route('/')
class MemberList(Resource):
    @api.doc('list members')
    @api.marshal_list_with(member)
    def get(self):
        return MEMBERS
