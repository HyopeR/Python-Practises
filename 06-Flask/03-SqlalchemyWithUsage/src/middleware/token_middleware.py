from flask import request
from functools import wraps
import jwt
from src.core.handlers.ErrorHandler import ErrorHandler
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from src.services.EnvironmentService import EnvironmentService


def token_middleware(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            error = ErrorDescriptive.token_is_missing
            raise ErrorHandler(error.message, error.key, 400)

        try:
            data = jwt.decode(token, EnvironmentService().get_one('SECRET_KEY'), algorithms=["HS256"])
        except Exception as e:
            error = ErrorDescriptive.token_invalid
            raise ErrorHandler(error.message, error.key, 400)

        return f(*args, **kwargs)

    return wrapper