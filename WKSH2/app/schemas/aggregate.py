from marshmallow import fields
from app.extensions import ma


class AllBuildingsSchema(ma.Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    type = fields.Str(required=True)
    country = fields.Str(required=True)
    city = fields.Str(required=True)
    year = fields.Int(required=True)
    height = fields.Float(required=True)

all_buildings_schema = AllBuildingsSchema(many=True)


class StatSchema(ma.Schema):
    id = fields.Int(load_default=None)
    name = fields.Str(load_default=None)
    year = fields.Int(load_default=None)
    avg_height = fields.Float(required=True)
    min_height = fields.Float(required=True)
    max_height = fields.Float(required=True)

stat_schema = StatSchema(many=True)
