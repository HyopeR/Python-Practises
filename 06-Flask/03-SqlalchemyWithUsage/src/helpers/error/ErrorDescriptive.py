from src.helpers.error.ErrorBase import ErrorBase


class ErrorDescriptive:
    # Task route error
    task_get = ErrorBase('task_get', 'An error occurred while fetching the task.')
    task_get_one = ErrorBase('task_get_one', 'An error occurred while fetching the task.')
    task_add = ErrorBase('task_add', 'Task update failed.')
    task_update = ErrorBase('task_update', 'Task update failed.')
    task_delete = ErrorBase('task_delete', 'ask deletion failed.')
