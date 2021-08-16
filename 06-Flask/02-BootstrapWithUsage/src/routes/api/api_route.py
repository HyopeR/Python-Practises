from flask import Blueprint, request
from src.routes.api.api_controller import ApiController
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.routes.api.api_schema import TrySchema

api = Blueprint('api', __name__, template_folder='../../templates')


@api.route("/api", methods=['GET'])
def get():
    return ApiController().get()


@api.route("/api/try", methods=['POST'])
@validate_json
@validate_schema(schema=TrySchema())
def post():
    body = request.get_json()
    print('BODY', body)

    return ApiController().post(body)
