from app.extensions import db
from app.models.country import Country
from app.models.city import City
from app.models.type_building import TypeBuilding
from app.models.buildings import Building
from sqlalchemy import func


def get_all_buildings():
    query = (
        db.session.query(
            Building.id,
            Building.title,
            TypeBuilding.name.label("type"),
            Country.name.label("country"),
            City.name.label("city"),
            Building.year,
            Building.height
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    return formatted_results


def get_stat_by_country():
    query = (
        db.session.query(
            Country.id,
            Country.name,
            func.avg(Building.height).label("avg_height"),
            func.min(Building.height).label("min_height"),
            func.max(Building.height).label("max_height")
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .group_by(Country.id, Country.name)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    return formatted_results


def get_stat_by_type():
    query = (
        db.session.query(
            TypeBuilding.id,
            TypeBuilding.name,
            func.avg(Building.height).label("avg_height"),
            func.min(Building.height).label("min_height"),
            func.max(Building.height).label("max_height")
        )
        .select_from(Building)
        .join(TypeBuilding)
        .group_by(TypeBuilding.id, TypeBuilding.name)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    return formatted_results


def get_stat_by_year():
    query = (
        db.session.query(
            Building.id,
            Building.year,
            func.avg(Building.height).label("avg_height"),
            func.min(Building.height).label("min_height"),
            func.max(Building.height).label("max_height")
        )
        .select_from(Building)
        .group_by(Building.id, Building.year)
        .order_by(Building.year)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    return formatted_results
