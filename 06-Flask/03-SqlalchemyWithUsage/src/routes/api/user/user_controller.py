from src.core.metaclass.Singleton import Singleton
from src.routes.api.user.user_service import UserService


class UserController(metaclass=Singleton):
    def __init__(self):
        self.UserService = UserService()

    def get(self):
        result = self.UserService.get()
        return result

    def get_one(self, id):
        result = self.UserService.get_one(id)
        return result

    def put(self, id, body):
        result = self.UserService.put(id, body)
        return result

    def delete(self, id):
        result = self.UserService.delete(id)
        return result
