from src.core.metaclass.Singleton import Singleton
from src.core.parentclass.Service import Service
from src.core.decorators.exception_catcher import exception_catcher


class TaskService(Service, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.Task = self.ModelModule.getModel("Task")

    @exception_catcher
    def get(self):
        data = self.Task.query.all()
        return {}

    @exception_catcher
    def get_one(self, id):
        return {}

    @exception_catcher
    def post(self, body):
        return {}

    @exception_catcher
    def put(self, id, body):
        return {}

    @exception_catcher
    def delete(self, id):
        return {}
