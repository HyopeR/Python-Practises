from src.core.metaclass.Singleton import Singleton
from src.core.parentclass.Service import Service
from src.core.decorators.service_interceptor import service_interceptor
from src.helpers.error.ErrorDescriptive import ErrorDescriptive


class CategoryService(Service, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.Category, = self.getModels(["Category"])
        self.category_schema, self.categories_schema = self.getSchemas(["Category", "Categories"])

    @service_interceptor(ErrorDescriptive.category_get.key)
    def get(self):
        data = self.Category.query.all()

        return self.categories_schema.dump(data)

    @service_interceptor(ErrorDescriptive.category_get_one.key)
    def get_one(self, id):
        find_category = self.Category.query.filter_by(id=id).first()

        return self.category_schema.dump(find_category)

    @service_interceptor(ErrorDescriptive.category_add.key)
    def post(self, body):
        new_category = self.Category(**body)
        self.db.session.add(new_category)
        self.db.session.commit()

        return self.category_schema.dump(new_category)

    @service_interceptor(ErrorDescriptive.category_update.key)
    def put(self, id, body):
        update = self.Category.query.filter_by(id=id).update(body, synchronize_session='fetch')
        updated_category = self.Category.query.filter_by(id=id).first()
        self.db.session.commit()

        return self.category_schema.dump(updated_category)

    @service_interceptor(ErrorDescriptive.category_delete.key)
    def delete(self, id):
        category = self.Category.query.filter_by(id=id).first()
        self.db.session.delete(category)
        self.db.session.commit()

        return self.category_schema.dump(category)
