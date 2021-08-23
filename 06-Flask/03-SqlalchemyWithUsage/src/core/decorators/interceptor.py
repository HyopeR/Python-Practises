from functools import wraps
from src.helpers.error.ErrorDescriptive import ErrorBase
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from src.core.handlers.ErrorHandler import ErrorHandler
from src.core.handlers.DataHandler import DataHandler


def interceptor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return DataHandler(result, 200).handle()

        except Exception as error:
            key = error.args[0]
            error_base: ErrorBase = getattr(ErrorDescriptive, key)
            detail = error.args[1]

            raise ErrorHandler(error_base.message, error_base.key, 400, detail)

    return wrapper
