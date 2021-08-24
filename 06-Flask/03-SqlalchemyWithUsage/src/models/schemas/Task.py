from manage import ma
from src.models.Task import Task
from src.models.schemas.Category import categories_schema
from marshmallow import fields


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # model = Task
        # include_relationships = True
        # include_fk = True
        ordered = True

    id = fields.Integer()
    title = fields.Str()
    content = fields.Str()
    steps = fields.Dict()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    is_done = fields.Bool()
    categories = fields.Nested(categories_schema)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
