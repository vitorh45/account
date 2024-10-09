from flask import Blueprint, request
from flask_restx import Api, Resource, marshal
from werkzeug.exceptions import Unauthorized
from flask_jwt_extended import jwt_required, get_jwt_identity

from .schemas import (
    token_response_model
)
from .decorators import validate_role
from api.domain.entities.user import User, UserNotFound, UserCredentialsInvalid
from api.domain.repositories.user_repository import SQLAlchemyUserRepository


VERSION = "0.0.1"
DOC = "Accounttest API"

blueprint = Blueprint("user", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version=VERSION,
    title="Accounttest API",
    description=f"{DOC} - User",
    doc="/docs/swagger"
)

ns = api.namespace("", description=DOC)

# ns.add_model(index_model.name, index_model)


@ns.route("/token")
class Token(Resource):
    @ns.response(200, "OK", token_response_model)
    def post(self) -> tuple[dict, int]:
        try:
            token = User.authenticate(
                username=request.json.get("username"),
                password=request.json.get("password"),
                repository=SQLAlchemyUserRepository)
        except (UserNotFound, UserCredentialsInvalid) as e:
            return {
                "message": str(e)
            }, 401
        return marshal({"token": token}, token_response_model), 200


@ns.route("/user")
class UserData(Resource):
    @ns.response(200, "OK")
    @jwt_required()
    @validate_role("user")
    def get(self) -> tuple[dict, int]:
        return {"message": "OK"}, 200
        

@ns.route("/admin")
class AdminData(Resource):
    @ns.response(200, "OK")
    @jwt_required()
    @validate_role("admin")
    def get(self) -> tuple[dict, int]:
        return {"message": "OK"}, 200