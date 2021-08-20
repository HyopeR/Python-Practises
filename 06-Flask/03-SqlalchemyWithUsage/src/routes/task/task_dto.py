from marshmallow import Schema, fields


class TaskPostDto(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=False)
    steps = fields.Mapping(required=False)


class TaskPutDto(Schema):
    title = fields.Str(required=False)
    content = fields.Str(required=False)
    steps = fields.Mapping(required=False)
