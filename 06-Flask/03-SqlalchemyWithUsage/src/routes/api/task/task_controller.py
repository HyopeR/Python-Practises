from src.core.metaclass.Singleton import Singleton
from src.routes.api.task.task_service import TaskService


class TaskController(metaclass=Singleton):
    def __init__(self):
        self.TaskService = TaskService()

    def get(self):
        result = self.TaskService.get()
        return result

    def get_one(self, id):
        result = self.TaskService.get_one(id)
        return result

    def post(self, body):
        categories = body.get('categories')
        if categories is not None and isinstance(categories, list):
            body.pop("categories")

        result = self.TaskService.post(body, categories)
        return result

    def put(self, id, body):
        categories = body.get('categories')

        if categories is not None and isinstance(categories, list):
            body.pop("categories")

        result = self.TaskService.put(id, body, categories)
        return result

    def delete(self, id):
        result = self.TaskService.delete(id)
        return result
