from functools import wraps
from flask import request
from src.core.handlers.ErrorHandler import ErrorHandler
from marshmallow import ValidationError, Schema


def validate_schema(schema):
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kw):
            data = request.get_json()

            try:
                schema.load(data)

            except ValidationError as err:
                raise ErrorHandler("DTO error", "dto_error", detail=err.messages)

            return f(*args, **kw)
        return wrapper
    return decorator