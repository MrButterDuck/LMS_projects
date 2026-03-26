from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.models.buildings import Building
from app.extensions import db, auth
from app.schemas.building import buildings_cschema, building_cschema

building_bp = Blueprint('building', __name__)


@building_bp.route('/', methods=['GET'])
def get_buildings():
    buildings = Building.query.all()
    return jsonify({
        "success": True,
        "buildings": buildings_cschema.dump(buildings)
    }), 200


@building_bp.route('/<int:id>', methods=['GET'])
def get_one_building(id):
    building = Building.query.get(id)
    if not building:
        return jsonify({
            "success": False,
            "error": "Building not found"
        }), 404
    return jsonify({
        "success": True,
        "building": building_cschema.dump(building)
    }), 200


@building_bp.route('/', methods=['POST'])
@auth.login_required
def create_building():
    try:
        data = request.get_json()
        building  = building_cschema.load(data, session=db.session)
        db.session.add(building)
        db.session.commit()
        return jsonify({
            "success": True,
            "building": building_cschema.dump(building)
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


@building_bp.route('/<int:id>', methods=['PUT'])
@auth.login_required
def update_building(id):
    building = Building.query.get(id)
    if not building:
        return jsonify({
            "success": False,
            "error": "Building not found"
        }), 404
    try:
        data = request.get_json()
        if 'title' in data:
            building.title = data['title']
        if 'type_building_id' in data:
            building.type_building_id = data['type_building_id']
        if 'city_id' in data:
            building.city_id = data['city_id']
        if 'year' in data:
            building.year = data['year']
        if 'height' in data:
            building.height = data['height']
        db.session.commit()
        return jsonify({
            "success": True,
            "building": building_cschema.dump(building)
        }), 200
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


@building_bp.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_building(id):
    building = Building.query.get(id)
    if not building:
        return jsonify({
            "success": False,
            "error": "Building not found"
        }), 404
    try:
        db.session.delete(building)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": f"Building with id={id} deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
