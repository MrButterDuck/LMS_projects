from marshmallow import fields
from app.extensions import ma


class AllCarsSchema(ma.Schema):
    id = fields.Int(required=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    transmission = fields.Str(required=True)
    driven_wheels = fields.Str(required=True)
    vehicle_type = fields.Str(required=True)
    number_of_doors = fields.Int(load_default=None)
    engine_cylinders = fields.Int(load_default=None)
    engine_hp = fields.Float(load_default=None)

class StatByMakeSchema(ma.Schema):
    id = fields.Int(required=True)
    make = fields.Str(required=True)
    avg_hp = fields.Float(required=True)
    min_hp = fields.Float(required=True)
    max_hp = fields.Float(required=True)


class StatByTransmissionSchema(ma.Schema):
    id = fields.Int(required=True)
    transmission = fields.Str(required=True)
    avg_hp = fields.Float(required=True)
    min_hp = fields.Float(required=True)
    max_hp = fields.Float(required=True)


class StatByVehicleTypeSchema(ma.Schema):
    id = fields.Int(required=True)
    vehicle_type = fields.Str(required=True)
    avg_hp = fields.Float(required=True)
    min_hp = fields.Float(required=True)
    max_hp = fields.Float(required=True)


class StatByYearSchema(ma.Schema):
    year = fields.Int(required=True)
    avg_hp = fields.Float(required=True)
    min_hp = fields.Float(required=True)
    max_hp = fields.Float(required=True)
    
all_cars_schema = AllCarsSchema(many=True)
stat_by_make_schema = StatByMakeSchema(many=True)
stat_by_transmission_schema = StatByTransmissionSchema(many=True)
stat_by_vehicle_type_schema = StatByVehicleTypeSchema(many=True)
stat_by_year_schema = StatByYearSchema(many=True)
