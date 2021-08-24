from src.core.metaclass.Singleton import Singleton
from src.routes.api.category.category_service import CategoryService


class CategoryController(metaclass=Singleton):
    def __init__(self):
        self.CategoryService = CategoryService()

    def get(self):
        result = self.CategoryService.get()
        return result

    def get_one(self, id):
        result = self.CategoryService.get_one(id)
        return result

    def post(self, body):
        result = self.CategoryService.post(body)
        return result

    def put(self, id, body):
        result = self.CategoryService.put(id, body)
        return result

    def delete(self, id):
        result = self.CategoryService.delete(id)
        return result
