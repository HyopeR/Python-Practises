from src.core.metaclass.Singleton import Singleton
from src.routes.task.task_service import TaskService


class TaskController(metaclass=Singleton):
    def __init__(self):
        self.TaskSer = TaskService()

    def get(self):
        self.TaskSer.get()
        return {}

    def get_one(self, id):
        self.TaskSer.get_one(id)
        return {}

    def post(self, body):
        self.TaskSer.post(body)
        return {}

    def put(self, id, body):
        self.TaskSer.put(id, body)
        return {}

    def delete(self, id):
        self.TaskSer.delete(id)
        return {}
