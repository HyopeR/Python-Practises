from flask import request
from functools import wraps
from src.core.handlers.ErrorHandler import ErrorHandler
from src.helpers.error.ErrorDescriptive import ErrorDescriptive


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if not data:
            error_base = ErrorDescriptive.invalid_json
            raise ErrorHandler(error_base.message, error_base.key, 400)

        return f(*args, **kwargs)

    return wrapper