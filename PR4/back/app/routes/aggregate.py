from flask import Blueprint, jsonify
from app.schemas.aggregate_schema import (
    all_cars_schema,
    stat_by_make_schema,
    stat_by_transmission_schema,
    stat_by_vehicle_type_schema,
    stat_by_year_schema
)
from app.models.aggregate import (
    get_all_cars,
    get_stat_by_make,
    get_stat_by_transmission,
    get_stat_by_vehicle_type,
    get_stat_by_year
)

aggregate_bp = Blueprint('aggregate', __name__)

@aggregate_bp.route('/all/', methods=['GET'])
def all_cars():
    results = get_all_cars()
    return jsonify({
        "success": True,
        "all_cars": all_cars_schema.dump(results)
    }), 200

@aggregate_bp.route('/make/', methods=['GET'])
def stat_by_make():
    results = get_stat_by_make()
    return jsonify({
        "success": True,
        "stat": stat_by_make_schema.dump(results)
    }), 200

@aggregate_bp.route('/transmission/', methods=['GET'])
def stat_by_transmission():
    results = get_stat_by_transmission()
    return jsonify({
        "success": True,
        "stat": stat_by_transmission_schema.dump(results)
    }), 200

@aggregate_bp.route('/vehicle-type/', methods=['GET'])
def stat_by_vehicle_type():
    results = get_stat_by_vehicle_type()
    return jsonify({
        "success": True,
        "stat": stat_by_vehicle_type_schema.dump(results)
    }), 200

@aggregate_bp.route('/year/', methods=['GET'])
def stat_by_year():
    results = get_stat_by_year()
    return jsonify({
        "success": True,
        "stat": stat_by_year_schema.dump(results)
    }), 200