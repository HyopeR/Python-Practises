from functools import wraps

def exception_catcher(error_key):
    def decorator(func):

        @wraps(func)
        def wrapper(self, *method_args, **method_kwargs):

            try:
                result = func(self, *method_args, **method_kwargs)
                return result

            except Exception as error:
                error.args = (error_key, *error.args)
                raise error

        return wrapper
    return decorator