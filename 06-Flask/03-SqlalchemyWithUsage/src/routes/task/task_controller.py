from src.core.metaclass.Singleton import Singleton
from src.routes.task.task_service import TaskService


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
        result = self.TaskService.post(body)
        return result

    def put(self, id, body):
        result = self.TaskService.put(id, body)
        return result

    def delete(self, id):
        result = self.TaskService.delete(id)
        return result
