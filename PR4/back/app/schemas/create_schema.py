# app/schemas/car_model_create_schema.py
from marshmallow import Schema, fields, post_load
from app import db
from app.models import *

class CarModelCreateSchema(Schema):
    make = fields.String(required=True)
    model = fields.String(required=True)
    year = fields.Integer(required=True)
    engine_hp = fields.Float(required=True)
    engine_cylinders = fields.Integer(required=True)
    transmission = fields.String(required=True)
    driven_wheels = fields.String(required=True)
    number_of_doors = fields.Integer(required=True)
    market_categories = fields.String(required=True)
    vehicle_type = fields.String(required=True)

    @post_load
    def make_obj(self, data, **kwargs):
        make = CarMake.query.filter_by(name=data['make']).first()
        if not make:
            make = CarMake(name=data['make'])
            db.session.add(make)
            db.session.flush()

        model = CarModel.query.filter_by(
            name=data['model'],
            make_id=make.id
        ).first()

        if not model:
            model = CarModel(name=data['model'], make_id=make.id)
            db.session.add(model)
            db.session.flush()

        transmission = TransmissionTypes.query.filter_by(
            name=data['transmission']
        ).first()
        if not transmission:
            transmission = TransmissionTypes(name=data['transmission'])
            db.session.add(transmission)
            db.session.flush()

        driven = DrivenWheelsTypes.query.filter_by(
            name=data['driven_wheels']
        ).first()
        if not driven:
            driven = DrivenWheelsTypes(name=data['driven_wheels'])
            db.session.add(driven)
            db.session.flush()

        vehicle = VehicleTypes.query.filter_by(
            name=data['vehicle_type']
        ).first()
        if not vehicle:
            vehicle = VehicleTypes(name=data['vehicle_type'])
            db.session.add(vehicle)
            db.session.flush()

        feature = CarFeatures(
            model_id=model.id,
            year=data['year'],
            transmission_id=transmission.id,
            driven_wheels_id=driven.id,
            vehicle_type_id=vehicle.id,
            number_of_doors=data['number_of_doors'],
            engine_cylinders=data['engine_cylinders'],
            engine_hp=data['engine_hp']
        )
        db.session.add(feature)

        categories = [x.strip() for x in data['market_categories'].split(',')]
        for cat_name in categories:
            cat = CategoryTypes.query.filter_by(name=cat_name).first()
            if not cat:
                cat = CategoryTypes(name=cat_name)
                db.session.add(cat)
                db.session.flush()

            exists = MarketCategory.query.filter_by(
                category_id=cat.id,
                model_id=model.id
            ).first()

            if not exists:
                db.session.add(MarketCategory(
                    category_id=cat.id,
                    model_id=model.id
                ))

        return model
    
car_model_create_schema = CarModelCreateSchema()