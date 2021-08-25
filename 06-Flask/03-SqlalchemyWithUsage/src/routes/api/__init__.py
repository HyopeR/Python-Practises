from flask import Blueprint, request

# Token Middleware
from src.middleware.token_middleware import token_middleware

# Api Routes
from src.routes.api.task.task_route import task_route
from src.routes.api.category.category_route import category_route
from src.routes.api.user.user_route import user_route

api_route = Blueprint('api', __name__, template_folder='../../templates', url_prefix='/api')
api_route.register_blueprint(task_route)
api_route.register_blueprint(category_route)
api_route.register_blueprint(user_route)


@api_route.before_request
@token_middleware
def token_base_middleware():
    pass
