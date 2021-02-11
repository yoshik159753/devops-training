import json

from flask import Response, request
from flask_restful import Resource
from src.core.json import default_handler
from src.database.models.user import User


class UsersApi(Resource):
    def post(self):
        request_body = request.get_json() if request.get_json() is not None else {}
        user = User(name=request_body.get("name"),
                    email=request_body.get("email"),
                    password=request_body.get("password"),
                    password_confirmation=request_body.get("password_confirmation"))
        if user.save() is False:
            errors = [{"message": error["message"]} for error in user.errors]
            response_body = {"summary": "Saving the user failed.",
                             "errors": errors}
            return Response(json.dumps(response_body), mimetype="application/json", status=400, headers={})

        response_body = {"id": user.id}
        return Response(json.dumps(response_body), mimetype="application/json", status=200, headers={})

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
