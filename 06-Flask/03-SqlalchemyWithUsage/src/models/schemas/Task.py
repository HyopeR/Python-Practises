from manage import ma
from src.models.Task import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True
        ordered = True
        # dump_only = ("created_at", "updated_at")


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
