from marshmallow import Schema, fields, validate


# Validation


class BaseUser(Schema):  # Schema inherits Schema from marshmallow
    # BaseUser represents the login with email and password because the user
    # will be logging in with email and password
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class ComplainerLoginRequestSchema(BaseUser):
    pass


class ComplainerRegisterRequestSchema(
    BaseUser
):  # for complainer model for register activity
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=3, max=13))
    iban = fields.String(required=True, validate=validate.Length(min=22, max=22))
