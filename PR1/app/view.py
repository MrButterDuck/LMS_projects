from flask import Blueprint, render_template
from sqlalchemy import func
from .extensions import db
from .models import (CarMake, CarModel, CategoryTypes,
                     MarketCategory, TransmissionTypes,
                     DrivenWheelsTypes, VehicleTypes, CarFeatures)

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/makes')
def makes():
    result = db.session.query(CarMake.id, CarMake.name.label('Марка')).select_from(CarMake)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='makes', page_title='Марки', head=keys, body=rows)


@main.route('/models')
def models():
    result = db.session.query(CarModel.id, CarModel.name.label('Модель'), CarMake.name.label('Марка')).select_from(CarModel).join(CarMake, CarModel.make_id == CarMake.id)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='models', page_title='Модели', head=keys, body=rows)


@main.route('/categories')
def categories():
    result = db.session.query(CategoryTypes.id, CategoryTypes.name.label('Категория')).select_from(CategoryTypes)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='categories', page_title='Категории', head=keys, body=rows)


@main.route('/market')
def market():
    result = db.session.query(CarModel.id, CarMake.name.label('Марка'), CarModel.name.label('Модель'), func.string_agg(CategoryTypes.name.distinct(), ', ').label('Категории'))\
        .select_from(MarketCategory)\
        .join(CarModel, MarketCategory.model_id == CarModel.id)\
        .join(CarMake, CarModel.make_id == CarMake.id)\
        .join(CategoryTypes, MarketCategory.category_id == CategoryTypes.id)\
        .group_by(CarModel.id, CarMake.name, CarModel.name)\
        .order_by(CarMake.name, CarModel.name)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='market', page_title='Рыночные категории', head=keys, body=rows)


@main.route('/transmissions')
def transmissions():
    result = db.session.query(TransmissionTypes.id, TransmissionTypes.name.label('Трансмиссия')).select_from(TransmissionTypes)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='transmissions', page_title='Типы трансмиссий', head=keys, body=rows)


@main.route('/wheels')
def wheels():
    result = db.session.query(DrivenWheelsTypes.id, DrivenWheelsTypes.name.label('Привод')).select_from(DrivenWheelsTypes)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='wheels', page_title='Типы привода', head=keys, body=rows)


@main.route('/vehicles')
def vehicles():
    result = db.session.query(VehicleTypes.id, VehicleTypes.name.label('Тип кузова')).select_from(VehicleTypes)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='vehicles', page_title='Типы кузова', head=keys, body=rows)


@main.route('/features')
def features():
    result = db.session.query(
        CarFeatures.id,
        CarMake.name.label('Марка'),
        CarModel.name.label('Модель'),
        CarFeatures.year.label('Год'),
        TransmissionTypes.name.label('Трансмиссия'),
        DrivenWheelsTypes.name.label('Привод'),
        VehicleTypes.name.label('Тип кузова'),
        CarFeatures.number_of_doors.label('Дверей'),
        CarFeatures.engine_cylinders.label('Цилиндры'),
        CarFeatures.engine_hp.label('Мощность (HP)'))\
    .select_from(CarFeatures)\
    .join(CarModel, CarFeatures.model_id == CarModel.id)\
    .join(CarMake, CarModel.make_id == CarMake.id)\
    .join(TransmissionTypes, CarFeatures.transmission_id == TransmissionTypes.id)\
    .join(DrivenWheelsTypes, CarFeatures.driven_wheels_id == DrivenWheelsTypes.id)\
    .join(VehicleTypes, CarFeatures.vehicle_type_id == VehicleTypes.id)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='features', page_title='Характеристики автомобилей', head=keys, body=rows)


@main.route('/all')
def all_data():
    result = db.session.query(
        CarFeatures.id,
        CarMake.name.label('Марка'),
        CarModel.name.label('Модель'),
        CarFeatures.year.label('Год'),
        TransmissionTypes.name.label('Трансмиссия'),
        DrivenWheelsTypes.name.label('Привод'),
        VehicleTypes.name.label('Тип кузова'),
        CarFeatures.number_of_doors.label('Дверей'),
        CarFeatures.engine_cylinders.label('Цилиндры'),
        CarFeatures.engine_hp.label('Мощность (HP)'),
        func.string_agg(CategoryTypes.name.distinct(), ', ').label('Категории'))\
    .select_from(CarFeatures)\
    .join(CarModel, CarFeatures.model_id == CarModel.id)\
    .join(CarMake, CarModel.make_id == CarMake.id)\
    .join(TransmissionTypes, CarFeatures.transmission_id == TransmissionTypes.id)\
    .join(DrivenWheelsTypes, CarFeatures.driven_wheels_id == DrivenWheelsTypes.id)\
    .join(VehicleTypes, CarFeatures.vehicle_type_id == VehicleTypes.id)\
    .outerjoin(MarketCategory, MarketCategory.model_id == CarModel.id)\
    .outerjoin(CategoryTypes, MarketCategory.category_id == CategoryTypes.id)\
    .group_by(
        CarFeatures.id,
        CarMake.name,
        CarModel.name,
        CarFeatures.year,
        TransmissionTypes.name,
        DrivenWheelsTypes.name,
        VehicleTypes.name,
        CarFeatures.number_of_doors,
        CarFeatures.engine_cylinders,
        CarFeatures.engine_hp
    ).order_by(CarMake.name, CarModel.name, CarFeatures.year)
    keys = list(result.statement.columns.keys())
    rows = result.all()
    return render_template('index.html', active='all', page_title='Все данные', head=keys, body=rows)


@main.route('/queries')
def queries():
    # мощность > 300 с механикой
    q1 = db.session.query(CarMake.name.label('Марка'), CarModel.name.label('Модель'), CarFeatures.year.label('Год'), CarFeatures.engine_hp.label('Мощность (HP)'), TransmissionTypes.name.label('Трансмиссия'))\
        .select_from(CarFeatures)\
        .join(CarModel, CarFeatures.model_id == CarModel.id)\
        .join(CarMake, CarModel.make_id == CarMake.id)\
        .join(TransmissionTypes, CarFeatures.transmission_id == TransmissionTypes.id)\
        .filter(CarFeatures.engine_hp > 300)\
        .filter(TransmissionTypes.name == 'MANUAL')\
        .order_by(CarFeatures.engine_hp.desc())
    q1_keys = list(q1.statement.columns.keys())
    q1_rows = q1.all()
 
    #мощность на цилиндр
    q2 = db.session.query(CarMake.name.label('Марка'), CarModel.name.label('Модель'), CarFeatures.year.label('Год'), CarFeatures.engine_hp.label('Мощность (HP)'), CarFeatures.engine_cylinders.label('Цилиндры'), (CarFeatures.engine_hp / CarFeatures.engine_cylinders).label('HP на цилиндр'))\
        .select_from(CarFeatures)\
        .join(CarModel, CarFeatures.model_id == CarModel.id)\
        .join(CarMake, CarModel.make_id == CarMake.id)\
        .filter(CarFeatures.engine_cylinders != None)\
        .filter(CarFeatures.engine_cylinders > 0)\
        .filter(CarFeatures.engine_hp != None)\
        .order_by((CarFeatures.engine_hp / CarFeatures.engine_cylinders).desc())
    q2_keys = list(q2.statement.columns.keys())
    q2_rows = q2.all()
 
    #мощность по маркам
    q3 = db.session.query(CarMake.name.label('Марка'), func.count(CarFeatures.id).label('Кол-во моделей'), func.avg(CarFeatures.engine_hp).label('Средняя мощность (HP)'), func.max(CarFeatures.engine_hp).label('Макс мощность (HP)'), func.min(CarFeatures.engine_hp).label('Мин мощность (HP)'))\
        .select_from(CarFeatures)\
        .join(CarModel, CarFeatures.model_id == CarModel.id)\
        .join(CarMake, CarModel.make_id == CarMake.id)\
        .filter(CarFeatures.engine_hp != None)\
        .group_by(CarMake.name)\
        .order_by(func.avg(CarFeatures.engine_hp).desc())
    q3_keys = list(q3.statement.columns.keys())
    q3_rows = q3.all()
 
    #кузов с > 250 HP и задний привод
    q4 = db.session.query(VehicleTypes.name.label('Тип кузова'), DrivenWheelsTypes.name.label('Привод'), func.count(CarFeatures.id).label('Кол-во'), func.avg(CarFeatures.engine_hp).label('Средняя мощность (HP)'))\
        .select_from(CarFeatures)\
        .join(VehicleTypes, CarFeatures.vehicle_type_id == VehicleTypes.id)\
        .join(DrivenWheelsTypes, CarFeatures.driven_wheels_id == DrivenWheelsTypes.id)\
        .filter(DrivenWheelsTypes.name == 'rear wheel drive')\
        .filter(CarFeatures.engine_hp != None)\
        .group_by(VehicleTypes.name, DrivenWheelsTypes.name)\
        .having(func.avg(CarFeatures.engine_hp) > 250)\
        .order_by(func.avg(CarFeatures.engine_hp).desc())
    q4_keys = list(q4.statement.columns.keys())
    q4_rows = q4.all()
 
    #мощность выше средней по марке
    avg_hp_subq = db.session.query(CarModel.make_id, func.avg(CarFeatures.engine_hp).label('avg_hp'))\
        .join(CarFeatures, CarFeatures.model_id == CarModel.id)\
        .filter(CarFeatures.engine_hp != None)\
        .group_by(CarModel.make_id)\
     .subquery()
 
    q5 = db.session.query(CarMake.name.label('Марка'), CarModel.name.label('Модель'), CarFeatures.year.label('Год'), CarFeatures.engine_hp.label('Мощность (HP)'), avg_hp_subq.c.avg_hp.label('Средняя по марке'))\
        .select_from(CarFeatures)\
        .join(CarModel, CarFeatures.model_id == CarModel.id)\
        .join(CarMake, CarModel.make_id == CarMake.id)\
        .join(avg_hp_subq, avg_hp_subq.c.make_id == CarModel.make_id)\
        .filter(CarFeatures.engine_hp != None)\
        .filter(CarFeatures.engine_hp > avg_hp_subq.c.avg_hp)\
        .order_by(CarMake.name, CarFeatures.engine_hp.desc())
    q5_keys = list(q5.statement.columns.keys())
    q5_rows = q5.all()
 
    return render_template(
        'queries.html', active='queries',
        q1_title='1. Мощные авто (>300 HP) с механической КПП',
        q1_desc='Выборка связанных таблиц с фильтрацией и сортировкой по убыванию мощности.',
        q1_keys=q1_keys, q1_rows=q1_rows,
        q2_title='2. Мощность на цилиндр',
        q2_desc='Вычисление по строкам: HP / количество цилиндров.',
        q2_keys=q2_keys, q2_rows=q2_rows,
        q3_title='3. Статистика мощности по маркам',
        q3_desc='Группировка с агрегатными функциями: среднее, макс, мин.',
        q3_keys=q3_keys, q3_rows=q3_rows,
        q4_title='4. Типы кузова с задним приводом и средней мощностью > 250 HP',
        q4_desc='Группировка с фильтрацией по исходным записям (WHERE) и по сгруппированным значениям (HAVING).',
        q4_keys=q4_keys, q4_rows=q4_rows,
        q5_title='5. Модели мощнее средней по своей марке',
        q5_desc='Вложенный запрос: подзапрос вычисляет среднюю мощность по каждой марке.',
        q5_keys=q5_keys, q5_rows=q5_rows
    )