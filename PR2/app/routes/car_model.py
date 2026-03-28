from flask import Blueprint, jsonify, request
from app.models import CarModel, DrivenWheelsTypes, CarMake, CarFeatures, VehicleTypes, TransmissionTypes, CategoryTypes, MarketCategory
from app.extensions import db, auth
from app.schemas.car_model_schema import car_model_schema, car_models_schema
from app.schemas.create_schema import car_model_create_schema
from marshmallow import ValidationError

car_model_bp = Blueprint('car_model', __name__)

@car_model_bp.route('/', methods=['GET'])
def get_all_models():
    models = CarModel.query.all()
    return jsonify({
        "success": True,
        "car_models": car_models_schema.dump(models)
    }), 200

@car_model_bp.route('/<int:id>', methods=['GET'])
def get_one_model(id):
    model = CarModel.query.get(id)
    if not model:
        return jsonify({
            "success": False,
            "error": "CarModel not found"
        }), 404
    return jsonify({
        "success": True,
        "car_model": car_model_schema.dump(model)
    }), 200


@car_model_bp.route('/', methods=['POST'])
@auth.login_required
def create_model():
    try:
        data = request.get_json()
        model = car_model_create_schema.load(data)
        db.session.commit()
        return jsonify({
            "success": True,
            "car_model": car_model_schema.dump(model)
        }), 201

    except ValidationError as err:
        db.session.rollback()
        return jsonify({
            "success": False,
            "errors": err.messages
        }), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@car_model_bp.route('/<int:id>', methods=['PUT'])
@auth.login_required
def update_model(id):
    model = CarModel.query.get(id)
    if not model:
        return jsonify({
            "success": False,
            "error": "CarModel not found"
        }), 404

    try:
        data = request.get_json()
        if 'make' in data:
            make = CarMake.query.filter_by(name=data['make']).first()
            if not make:
                make = CarMake(name=data['make'])
                db.session.add(make)
                db.session.flush()
            model.make_id = make.id

        if 'model' in data:
            model.name = data['model']

        transmission = None
        if 'transmission' in data:
            transmission = TransmissionTypes.query.filter_by(name=data['transmission']).first()
            if not transmission:
                transmission = TransmissionTypes(name=data['transmission'])
                db.session.add(transmission)
                db.session.flush()

        driven = None
        if 'driven_wheels' in data:
            driven = DrivenWheelsTypes.query.filter_by(name=data['driven_wheels']).first()
            if not driven:
                driven = DrivenWheelsTypes(name=data['driven_wheels'])
                db.session.add(driven)
                db.session.flush()

        vehicle = None
        if 'vehicle_type' in data:
            vehicle = VehicleTypes.query.filter_by(name=data['vehicle_type']).first()
            if not vehicle:
                vehicle = VehicleTypes(name=data['vehicle_type'])
                db.session.add(vehicle)
                db.session.flush()

        existing_feature = None
        if 'year' in data:
            existing_feature = CarFeatures.query.filter_by(model_id=model.id,year=data['year']).first()

        if existing_feature:
            if transmission:
                existing_feature.transmission_id = transmission.id
            if driven:
                existing_feature.driven_wheels_id = driven.id
            if vehicle:
                existing_feature.vehicle_type_id = vehicle.id

            if 'engine_hp' in data:
                existing_feature.engine_hp = data['engine_hp']
            if 'engine_cylinders' in data:
                existing_feature.engine_cylinders = data['engine_cylinders']
            if 'number_of_doors' in data:
                existing_feature.number_of_doors = data['number_of_doors']
        else:
            feature = CarFeatures(
                model_id=model.id,
                year=data['year'],
                transmission_id=transmission.id if transmission else None,
                driven_wheels_id=driven.id if driven else None,
                vehicle_type_id=vehicle.id if vehicle else None,
                number_of_doors=data.get('number_of_doors'),
                engine_cylinders=data.get('engine_cylinders'),
                engine_hp=data.get('engine_hp')
            )
            db.session.add(feature)

        if 'market_categories' in data:
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

        db.session.commit()

        return jsonify({
            "success": True,
            "car_model": car_model_schema.dump(model)
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@car_model_bp.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_model(id):
    model = CarModel.query.get(id)
    if not model:
        return jsonify({
            "success": False,
            "error": "CarModel not found"
        }), 404
    try:
        db.session.delete(model)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": f"CarModel with id {id} deleted"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
