from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.routes.auth.auth_controller import AuthController
from src.routes.auth.auth_dto import UserLoginDto, UserRegisterDto
from src.core.decorators.interceptor import interceptor

auth_route = Blueprint('auth', __name__, template_folder='../../templates', url_prefix='/auth')


@auth_route.route("/login", methods=['POST'])
@validate_json
@validate_schema(UserLoginDto())
@interceptor
def login():
    body = request.get_json()
    return AuthController().login(body)


@auth_route.route("/register", methods=['POST'])
@validate_json
@validate_schema(UserRegisterDto())
@interceptor
def register():
    body = request.get_json()
    return AuthController().register(body)
