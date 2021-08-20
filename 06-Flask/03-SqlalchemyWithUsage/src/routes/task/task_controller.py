from src.core.metaclass.Singleton import Singleton
from src.routes.task.task_service import TaskService


class TaskController(metaclass=Singleton):
    def get(self):
        TaskService().get()
        return {}

    def get_one(self, id):
        TaskService().get_one(id)
        return {}

    def post(self, body):
        TaskService().post(body)
        return {}

    def put(self, id, body):
        TaskService().put(id, body)
        return {}

    def delete(self, id):
        TaskService().delete(id)
        return {}
