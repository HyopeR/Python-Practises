from src.helpers.error.ErrorBase import ErrorBase


class ErrorDescriptive:
    route_not_found = ErrorBase('route_not_found', 'Route is not found.')
    unexpected_error = ErrorBase('unexpected_error', 'Unexpected error.')
    dto_error = ErrorBase('dto_error', 'The data contained in the request body is missing or incorrect.')
    invalid_json = ErrorBase('invalid_json', 'Invalid request body. The data you send must be JSON.')
    authorized_error = ErrorBase('authorized_error', 'You are not authorized for this operation!')

    # Token error
    token_is_missing = ErrorBase('token_is_missing', 'A valid token is missing.')
    token_invalid = ErrorBase('token_invalid', 'Token is invalid.')

    # Auth error
    login_error = ErrorBase('login_error', 'Login failed.')
    register_error = ErrorBase('register_error', 'Register failed.')

    # Task route error
    task_get = ErrorBase('task_get', 'An error occurred while fetching the task.')
    task_get_one = ErrorBase('task_get_one', 'An error occurred while fetching the task.')
    task_add = ErrorBase('task_add', 'Task add failed.')
    task_update = ErrorBase('task_update', 'Task update failed.')
    task_delete = ErrorBase('task_delete', 'Task deletion failed.')

    # Category route error
    category_get = ErrorBase('category_get', 'An error occurred while fetching the category.')
    category_get_one = ErrorBase('category_get_one', 'An error occurred while fetching the category.')
    category_add = ErrorBase('category_add', 'Category add failed.')
    category_update = ErrorBase('category_update', 'Category update failed.')
    category_delete = ErrorBase('category_delete', 'Category deletion failed.')

    # User route error
    user_get = ErrorBase('user_get', 'An error occurred while fetching the user.')
    user_get_one = ErrorBase('user_get_one', 'An error occurred while fetching the user.')
    user_update = ErrorBase('user_update', 'User update failed.')
    user_delete = ErrorBase('user_delete', 'User deletion failed.')