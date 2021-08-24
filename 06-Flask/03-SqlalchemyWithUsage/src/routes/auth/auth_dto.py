from marshmallow import Schema, fields


class UserLoginDto(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class UserRegisterDto(Schema):
    name = fields.Str(required=True)
    surname = fields.Str(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)
