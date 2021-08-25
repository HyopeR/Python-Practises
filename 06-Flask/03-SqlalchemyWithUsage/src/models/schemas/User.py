from manage import ma
from src.models.schemas.Task import tasks_schema
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # model = Task
        # include_relationships = True
        # include_fk = True
        ordered = True

    id = fields.Integer()
    user_id = fields.Integer(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    email = fields.Str()
    password = fields.Str(load_only=True)
    active = fields.Bool()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    tasks = fields.Nested(tasks_schema)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
