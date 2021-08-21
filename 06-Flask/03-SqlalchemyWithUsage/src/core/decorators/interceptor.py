from functools import wraps
from src.helpers.error.ErrorDescriptive import ErrorBase
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from src.core.handlers.ErrorHandler import ErrorHandler


def interceptor(func):
    print('this is executed at function definition time (def my_func)')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('this is executed before function call')
        try:
            result = func(*args, **kwargs)
            print('this is executed after function call')
            return result
        except Exception as error:
            detail: ErrorBase = getattr(ErrorDescriptive, str(error))
            raise ErrorHandler(detail.message, detail.key, 400)

    return wrapper
