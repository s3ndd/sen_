from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.UUID(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    username = fields.String()
    password = fields.String()
    email = fields.Email()
    mobile = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    is_active = fields.Boolean()
