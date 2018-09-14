#THIRD-PARTY IMPORTS
from marshmallow import (Schema, fields)

# URBVAN IMPORTS
from apps.stations.v1.schemas import StationSchema


class LineSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):

    id = fields.String()
    line = fields.Nested(LineSchema)
    station = fields.Nested(StationSchema)
    direction = fields.Boolean()
    is_active = fields.Boolean()