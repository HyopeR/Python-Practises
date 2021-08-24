from marshmallow import Schema, fields


class CategoryPostDto(Schema):
    title = fields.Str(required=True)


class CategoryPutDto(Schema):
    title = fields.Str(required=False)
