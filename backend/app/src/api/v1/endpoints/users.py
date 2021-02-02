import json

from flask import Response
from flask_restful import Resource
from src.core.json import default_handler
from src.database.models.user import User


class UsersApi(Resource):
    def get(self):
        return None, 500


class UserApi(Resource):
    def get(self, user_id):
        user = User.find_by(id=user_id)
        response_body = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        }
        return Response(json.dumps(response_body, default=default_handler),
                        mimetype="application/json",
                        status=200,
                        headers={})
