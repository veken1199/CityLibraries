from marshmallow import fields, Schema


class BaseResponseSchema(Schema):
    """
    This is the base schema for all response schema in the app
    All api responses must have message and has_error fields
    The children will extend and add special field to the base request
    """
    message = fields.Dict()
    has_error = fields.Boolean()