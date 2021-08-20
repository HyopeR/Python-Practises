from src.core.metaclass.Singleton import Singleton
from src.services.AlchemyService import AlchemyService
from src.services.ModelService import ModelService


class TaskService(metaclass=Singleton):
    def __init__(self):
        self.db = AlchemyService().db
        self.Task = ModelService().getModel()

    def get(self):
        ModelService().getModel()
        # data = Task.query.all()
        return {}

    def get_one(self, id):
        return {}

    def post(self, body):
        return {}

    def put(self, id, body):
        return {}

    def delete(self, id):
        return {}