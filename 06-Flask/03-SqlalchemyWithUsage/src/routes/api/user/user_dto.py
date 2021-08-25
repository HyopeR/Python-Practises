from marshmallow import Schema, fields


class UserPutDto(Schema):
    name = fields.Str(required=False)
    surname = fields.Str(required=False)
    email = fields.Email(required=False)
    password = fields.Str(required=False)
    active = fields.Bool(required=False)
