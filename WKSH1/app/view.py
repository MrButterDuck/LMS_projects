from flask import Blueprint, render_template
from .models import TypeBuilding, Country, City, Building
from .extensions import db
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/types')
def type_buildings():
    result = (db.session.query(TypeBuilding.id, TypeBuilding.name.label("Тип здания")).select_from(TypeBuilding))
    return render_template('index.html', active='types', page_title='Типы зданий', head=result.statement.columns.keys(), body=result.all())

@main.route('/countries')
def countries():
    result = (db.session.query(Country.id, Country.name.label("Страна")).select_from(Country))
    return render_template('index.html', active='countries', page_title='Страны', head=result.statement.columns.keys(), body=result.all())

@main.route('/cities')
def cities():
    result = (db.session.query(City.id, City.name.label("Город"), Country.name.label("Страна")).select_from(City).join(Country, City.country_id == Country.id))
    return render_template('index.html', active='cities', page_title='Города', head=result.statement.columns.keys(), body=result.all())

@main.route('/buildings')
def buildings():
    result = (db.session.query(Building.id, Building.title.label("Название"), TypeBuilding.name.label("Тип здания"), City.name.label("Город"), Country.name.label("Страна"), Building.year.label("Год постройки"), Building.height.label("Высота"))
        .select_from(Building)
        .join(TypeBuilding, Building.type_building_id == TypeBuilding.id)
        .join(City, Building.city_id == City.id)
        .join(Country, City.country_id == Country.id)
    )
    return render_template('index.html', active='buildings', page_title='Здания и сооружения', head=result.statement.columns.keys(), body=result.all())


@main.route('/stats')
def stats():
    by_type = (
        db.session.query(TypeBuilding.name.label("Тип"), func.max(Building.height).label("Максимальная высота"), func.min(Building.height).label("Минимальная высота"), func.round(func.avg(Building.height), 1).label("Средняя высота"))
        .select_from(Building)
        .join(TypeBuilding, Building.type_building_id == TypeBuilding.id)
        .group_by(TypeBuilding.name)
        .order_by(TypeBuilding.name)
    )

    by_country = (db.session.query(Country.name.label("Страна"), func.max(Building.height).label("Максимальная высота"), func.min(Building.height).label("Минимальная высота"), func.round(func.avg(Building.height), 1).label("Средняя высота"))
        .select_from(Building)
        .join(City, Building.city_id == City.id)
        .join(Country, City.country_id == Country.id)
        .group_by(Country.name)
        .order_by(Country.name)
    )

    by_city = (db.session.query(City.name.label("Город"), Country.name.label("Страна"), func.max(Building.height).label("Максимальная высота"), func.min(Building.height).label("Минимальная высота"), func.round(func.avg(Building.height), 1).label("Средняя высота"))
        .select_from(Building)
        .join(City, Building.city_id == City.id)
        .join(Country, City.country_id == Country.id)
        .group_by(City.name, Country.name)
        .order_by(City.name)
    )

    return render_template('stats.html', active='stats', by_type_head=by_type.statement.columns.keys(), by_type_body=by_type.all(), by_country_head=by_country.statement.columns.keys(), by_country_body=by_country.all(), by_city_head=by_city.statement.columns.keys(), by_city_body=by_city.all())