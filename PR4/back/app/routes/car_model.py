from flask import Blueprint, jsonify, request
from app.models import CarModel, DrivenWheelsTypes, CarMake, CarFeatures, VehicleTypes, TransmissionTypes, CategoryTypes, MarketCategory
from app.extensions import db, auth
from app.schemas.car_model_schema import car_model_schema, car_models_schema
from app.schemas.create_schema import car_model_create_schema
from marshmallow import ValidationError

car_model_bp = Blueprint('car_model', __name__)

@car_model_bp.route('/', methods=['GET'])
def get_all_models():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    search = request.args.get("search")

    from app.models.aggregate import get_all_cars
    all_cars = get_all_cars()

    filters = []

    for key in request.args:
        if key.startswith("filter[") and key.endswith("]"):
            field = key[7:-1]
            value = request.args.get(key)
            operator = request.args.get(f"op[{field}]") or "contains"

            filters.append({
                "field": field,
                "value": value,
                "operator": operator
            })

    def apply_filter(car, field, value, operator):
        car_value = str(car.get(field, "")).lower()
        value = str(value).lower()

        if operator in ["equals"]:
            return car_value == value

        if operator in ["doesNotEqual", "not"]:
            return car_value != value

        if operator in ["startsWith"]:
            return car_value.startswith(value)

        if operator in ["endsWith"]:
            return car_value.endswith(value)

        if operator in ["isEmpty"]:
            return car_value == ""

        if operator in ["isNotEmpty"]:
            return car_value != ""
        
        if operator in ["doesNotContain"]:
            return car_value not in value

        if operator in ["contains"]:
            return car_value in value

        return value in car_value

    filtered_cars = all_cars

    for f in filters:
        if f["value"] is not None and f["value"] != "":
            filtered_cars = [
                car for car in filtered_cars
                if apply_filter(car, f["field"], f["value"], f["operator"])
            ]

    if search:
        search = search.lower()

        def match_row(car):
            return search in " ".join(
                str(v).lower()
                for v in car.values()
                if v is not None
            )

        filtered_cars = [
            car for car in filtered_cars
            if match_row(car)
        ]

    total = len(filtered_cars)

    start = (page - 1) * limit
    end = start + limit

    paginated_cars = filtered_cars[start:end]

    return jsonify({
        "success": True,
        "car_models": paginated_cars,
        "total": total,
        "page": page,
        "limit": limit
    }), 200

@car_model_bp.route('/<int:id>', methods=['GET'])
def get_one_model(id):
    from app.models.aggregate import get_all_cars
    all_cars = get_all_cars()
    car = next((c for c in all_cars if c['id'] == id), None)
    
    if not car:
        return jsonify({
            "success": False,
            "error": "Car not found"
        }), 404
    
    return jsonify({
        "success": True,
        "car_model": car
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
def update_car_feature(id):
    feature = CarFeatures.query.get(id)
    if not feature:
        return jsonify({
            "success": False,
            "error": "Car feature not found"
        }), 404
    
    try:
        data = request.get_json()
        model = CarModel.query.get(feature.model_id)
        
        if 'make' in data:
            make = CarMake.query.filter_by(name=data['make']).first()
            if not make:
                make = CarMake(name=data['make'])
                db.session.add(make)
                db.session.flush()
            model.make_id = make.id

        if 'model' in data:
            model.name = data['model']

        if 'transmission' in data:
            transmission = TransmissionTypes.query.filter_by(name=data['transmission']).first()
            if not transmission:
                transmission = TransmissionTypes(name=data['transmission'])
                db.session.add(transmission)
                db.session.flush()
            feature.transmission_id = transmission.id

        if 'driven_wheels' in data:
            driven = DrivenWheelsTypes.query.filter_by(name=data['driven_wheels']).first()
            if not driven:
                driven = DrivenWheelsTypes(name=data['driven_wheels'])
                db.session.add(driven)
                db.session.flush()
            feature.driven_wheels_id = driven.id

        if 'vehicle_type' in data:
            vehicle = VehicleTypes.query.filter_by(name=data['vehicle_type']).first()
            if not vehicle:
                vehicle = VehicleTypes(name=data['vehicle_type'])
                db.session.add(vehicle)
                db.session.flush()
            feature.vehicle_type_id = vehicle.id

        if 'year' in data:
            feature.year = data['year']
        if 'engine_hp' in data:
            feature.engine_hp = data['engine_hp']
        if 'engine_cylinders' in data:
            feature.engine_cylinders = data['engine_cylinders']
        if 'number_of_doors' in data:
            feature.number_of_doors = data['number_of_doors']

        if 'market_categories' in data:
            old_categories = MarketCategory.query.filter_by(model_id=model.id).all()
            for old_cat in old_categories:
                db.session.delete(old_cat)
            
            categories = [x.strip() for x in data['market_categories'].split(',')]
            for cat_name in categories:
                cat = CategoryTypes.query.filter_by(name=cat_name).first()
                if not cat:
                    cat = CategoryTypes(name=cat_name)
                    db.session.add(cat)
                    db.session.flush()
                
                db.session.add(MarketCategory(
                    category_id=cat.id,
                    model_id=model.id
                ))

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Updated successfully"
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@car_model_bp.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_car_feature(id):
    feature = CarFeatures.query.get(id)
    if not feature:
        return jsonify({
            "success": False,
            "error": "Car feature not found"
        }), 404
    
    try:
        db.session.delete(feature)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": f"Car feature with id {id} deleted"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@car_model_bp.route('/makes', methods=['GET'])
def get_makes():
    makes = CarMake.query.all()
    return jsonify({
        "success": True,
        "makes": [{"id": m.id, "name": m.name} for m in makes]
    }), 200

@car_model_bp.route('/vehicle-types', methods=['GET'])
def get_vehicle_types():
    types = VehicleTypes.query.all()
    return jsonify({
        "success": True,
        "vehicle_types": [{"id": t.id, "name": t.name} for t in types]
    }), 200

@car_model_bp.route('/transmissions', methods=['GET'])
def get_transmissions():
    transmissions = TransmissionTypes.query.all()
    return jsonify({
        "success": True,
        "transmissions": [{"id": t.id, "name": t.name} for t in transmissions]
    }), 200

@car_model_bp.route('/driven-wheels', methods=['GET'])
def get_driven_wheels():
    wheels = DrivenWheelsTypes.query.all()
    return jsonify({
        "success": True,
        "driven_wheels": [{"id": w.id, "name": w.name} for w in wheels]
    }), 200

@car_model_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = CategoryTypes.query.all()
    return jsonify({
        "success": True,
        "categories": [{"id": c.id, "name": c.name} for c in categories]
    }), 200