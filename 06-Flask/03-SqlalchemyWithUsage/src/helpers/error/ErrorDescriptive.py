from src.helpers.error.ErrorBase import ErrorBase


class ErrorDescriptive:
    route_not_found = ErrorBase('route_not_found', 'Route is not found.')
    unexpected_error = ErrorBase('unexpected_error', 'Unexpected error.')
    dto_error = ErrorBase('dto_error', 'Unexpected error.')
    invalid_json = ErrorBase('invalid_json', 'Unexpected error.')

    # Task route error
    task_get = ErrorBase('task_get', 'An error occurred while fetching the task.')
    task_get_one = ErrorBase('task_get_one', 'An error occurred while fetching the task.')
    task_add = ErrorBase('task_add', 'Task update failed.')
    task_update = ErrorBase('task_update', 'Task update failed.')
    task_delete = ErrorBase('task_delete', 'ask deletion failed.')
