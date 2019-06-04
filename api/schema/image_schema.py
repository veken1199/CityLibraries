from .base_schema import BaseResponseSchema
from marshmallow import Schema, fields


class ImageSchema(Schema):
    """
    The image records from database will be deserialized to this this type
    and then will be sent to the client as array of images using ImageResponseSchema
    """
    image_url = fields.String()
    title = fields.String()
    description = fields.String()
    posted_on = fields.String()

class ImageResponseSchema(BaseResponseSchema):
    """
    This class is responsible for representing image response to our clients
    """
    data = fields.Nested(ImageSchema, many=True)

