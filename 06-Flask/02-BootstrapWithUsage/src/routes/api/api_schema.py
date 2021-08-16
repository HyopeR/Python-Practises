from marshmallow import Schema, fields


class TrySchema(Schema):
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
