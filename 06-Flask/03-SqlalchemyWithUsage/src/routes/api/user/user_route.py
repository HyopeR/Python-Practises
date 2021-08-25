from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.utils.decorators.interceptor import interceptor
from src.routes.api.user.user_dto import UserPutDto
from src.routes.api.user.user_controller import UserController

user_route = Blueprint('user', __name__, template_folder='../../templates')


@user_route.route("/user", methods=['GET'])
@interceptor
def get():
    return UserController().get()


@user_route.route("/user/<int:id>", methods=['GET'])
@interceptor
def get_one(id):
    return UserController().get_one(id)


@user_route.route("/user/<int:id>", methods=['PUT'])
@validate_json
@validate_schema(schema=UserPutDto())
@interceptor
def put(id):
    body = request.get_json()
    return UserController().put(id, body)


@user_route.route("/user/<int:id>", methods=['DELETE'])
@interceptor
def delete(id):
    return UserController().delete(id)
