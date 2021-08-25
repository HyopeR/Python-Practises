from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.utils.decorators.interceptor import interceptor
from src.routes.api.category.category_dto import CategoryPostDto, CategoryPutDto
from src.routes.api.category.category_controller import CategoryController

category_route = Blueprint('category', __name__, template_folder='../../templates')


@category_route.route("/category", methods=['GET'])
@interceptor
def get():
    return CategoryController().get()


@category_route.route("/category/<int:id>", methods=['GET'])
@interceptor
def get_one(id):
    return CategoryController().get_one(id)


@category_route.route("/category", methods=['POST'])
@validate_json
@validate_schema(schema=CategoryPostDto())
@interceptor
def post():
    body = request.get_json()
    return CategoryController().post(body)


@category_route.route("/category/<int:id>", methods=['PUT'])
@validate_json
@validate_schema(schema=CategoryPutDto())
@interceptor
def put(id):
    body = request.get_json()
    return CategoryController().put(id, body)


@category_route.route("/category/<int:id>", methods=['DELETE'])
@interceptor
def delete(id):
    return CategoryController().delete(id)
