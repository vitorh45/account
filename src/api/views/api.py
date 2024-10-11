from flask import Blueprint, request
from flask_restx import Api, Resource

from .schemas import (
    index_model,
    token_response_model,
    token_request_model
)
from .user import Token, UserData, AdminData

VERSION = "0.0.1"
DOC = "Accounttest API"

blueprint = Blueprint("index", __name__)

api = Api(
    blueprint,
    version=VERSION,
    title="Accounttest Index API",
    description=f"{DOC} - Index",
    doc="/docs/swagger"
)

ns = api.namespace("", description=DOC)

ns.add_model(index_model.name, index_model)
ns.add_model(token_response_model.name, token_response_model)
ns.add_model(token_request_model.name, token_request_model)

ns.add_resource(Token, "/token")
ns.add_resource(UserData, "/user")
ns.add_resource(AdminData, "/admin")


@ns.route("/health")
class Index(Resource):
    @ns.response(200, "OK", index_model)
    def get(self) -> tuple[dict, int]:
        return dict(
            service=DOC,
            version=VERSION
        ), 200
