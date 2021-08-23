from functools import wraps


def service_interceptor(error_key):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result

            except Exception as error:
                error.args = (error_key, *error.args)
                raise error

        return wrapper

    return decorator
