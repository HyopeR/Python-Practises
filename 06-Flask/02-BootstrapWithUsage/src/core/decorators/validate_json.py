from flask import request
from functools import wraps
from src.core.handlers.ErrorHandler import ErrorHandler


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if not data:
            raise ErrorHandler("Request body expected to JSON", "invalid_request_body")

        return f(*args, **kwargs)

    return wrapper