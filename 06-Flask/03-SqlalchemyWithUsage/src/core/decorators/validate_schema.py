from functools import wraps
from flask import request
from src.core.handlers.ErrorHandler import ErrorHandler
from marshmallow import ValidationError, Schema
from src.helpers.error.ErrorDescriptive import ErrorDescriptive


def validate_schema(schema):
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kw):
            data = request.get_json()

            try:
                schema.load(data)

            except ValidationError as err:
                error_base = ErrorDescriptive.dto_error
                raise ErrorHandler(error_base.message, error_base.key, 400, err.messages)

            return f(*args, **kw)

        return wrapper

    return decorator