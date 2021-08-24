from src.core.metaclass.Singleton import Singleton
from src.core.parentclass.Service import Service
from src.core.decorators.service_interceptor import service_interceptor
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from typing import Dict


class TaskService(Service, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.Task, self.Category = self.getModels(["Task", "Category"])
        self.task_schema, self.tasks_schema = self.getSchemas(["Task", "Tasks"])

    @service_interceptor(ErrorDescriptive.task_get.key)
    def get(self):
        data = self.Task.query.all()

        return self.tasks_schema.dump(data)

    @service_interceptor(ErrorDescriptive.task_get_one.key)
    def get_one(self, id):
        find_task = self.Task.query.filter_by(id=id).first()

        return self.task_schema.dump(find_task)

    @service_interceptor(ErrorDescriptive.task_add.key)
    def post(self, body: Dict, categories):
        new_task = self.Task(**body)

        if isinstance(categories, list):
            data = self.Category.query.filter(self.Category.id.in_(categories)).all()
            for category in data:
                new_task.categories.append(category)


        self.db.session.add(new_task)
        self.db.session.commit()

        return self.task_schema.dump(new_task)

    @service_interceptor(ErrorDescriptive.task_update.key)
    def put(self, id, body: Dict, categories):
        update = self.Task.query.filter_by(id=id).update(body, synchronize_session='fetch')
        updated_task = self.Task.query.filter_by(id=id).first()

        if isinstance(categories, list):
            updated_task.categories = []

            data = self.Category.query.filter(self.Category.id.in_(categories)).all()
            for category in data:
                updated_task.categories.append(category)

        self.db.session.commit()

        return self.task_schema.dump(updated_task)

    @service_interceptor(ErrorDescriptive.task_delete.key)
    def delete(self, id):
        task = self.Task.query.filter_by(id=id).first()
        self.db.session.delete(task)
        self.db.session.commit()

        return self.task_schema.dump(task)
