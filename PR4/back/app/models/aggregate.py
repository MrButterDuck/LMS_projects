from app.extensions import db
from app.models.car_make import CarMake
from app.models.car_model import CarModel
from app.models.car_features import CarFeatures
from app.models.transmission_types import TransmissionTypes
from app.models.driven_wheels_types import DrivenWheelsTypes
from app.models.vehicle_types import VehicleTypes
from app.models.market_category import MarketCategory
from app.models.category_types import CategoryTypes
from sqlalchemy import func, Numeric, cast


# полностью
def get_all_cars():
    query = (
        db.session.query(
            CarFeatures.id,
            CarMake.name.label('make'),
            CarModel.name.label('model'),
            CarFeatures.year,
            TransmissionTypes.name.label('transmission'),
            DrivenWheelsTypes.name.label('driven_wheels'),
            VehicleTypes.name.label('vehicle_type'),
            CarFeatures.number_of_doors,
            CarFeatures.engine_cylinders,
            CarFeatures.engine_hp,
            func.string_agg(CategoryTypes.name, ', ').label('categories')
        )
        .select_from(CarFeatures)
        .join(CarModel, CarFeatures.model_id == CarModel.id)
        .join(CarMake, CarModel.make_id == CarMake.id)
        .join(TransmissionTypes, CarFeatures.transmission_id == TransmissionTypes.id)
        .join(DrivenWheelsTypes, CarFeatures.driven_wheels_id == DrivenWheelsTypes.id)
        .join(VehicleTypes, CarFeatures.vehicle_type_id == VehicleTypes.id)
        .outerjoin(MarketCategory, CarFeatures.model_id == MarketCategory.model_id)
        .outerjoin(CategoryTypes, MarketCategory.category_id == CategoryTypes.id)
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
        )
        .order_by(CarMake.name, CarModel.name, CarFeatures.year)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    return [dict(zip(keys, row)) for row in results]


# мощность по марке
def get_stat_by_make():
    query = (
        db.session.query(
            CarMake.id,
            CarMake.name.label('make'),
            func.round(cast(func.avg(CarFeatures.engine_hp), Numeric), 2).label('avg_hp'),
            func.min(CarFeatures.engine_hp).label('min_hp'),
            func.max(CarFeatures.engine_hp).label('max_hp')
        )
        .select_from(CarFeatures)
        .join(CarModel, CarFeatures.model_id == CarModel.id)
        .join(CarMake, CarModel.make_id == CarMake.id)
        .group_by(CarMake.id, CarMake.name)
        .order_by(func.avg(CarFeatures.engine_hp).desc())
    )
    results = query.all()
    keys = query.statement.columns.keys()
    return [dict(zip(keys, row)) for row in results]


# мощность по трансмиссии
def get_stat_by_transmission():
    query = (
        db.session.query(
            TransmissionTypes.id,
            TransmissionTypes.name.label('transmission'),
            func.round(cast(func.avg(CarFeatures.engine_hp), Numeric), 2).label('avg_hp'),
            func.min(CarFeatures.engine_hp).label('min_hp'),
            func.max(CarFeatures.engine_hp).label('max_hp')
        )
        .select_from(CarFeatures)
        .join(TransmissionTypes, CarFeatures.transmission_id == TransmissionTypes.id)
        .group_by(TransmissionTypes.id, TransmissionTypes.name)
        .order_by(func.avg(CarFeatures.engine_hp).desc())
    )
    results = query.all()
    keys = query.statement.columns.keys()
    return [dict(zip(keys, row)) for row in results]


# мощность по кузову
def get_stat_by_vehicle_type():
    query = (
        db.session.query(
            VehicleTypes.id,
            VehicleTypes.name.label('vehicle_type'),
            func.round(cast(func.avg(CarFeatures.engine_hp), Numeric), 2).label('avg_hp'),
            func.min(CarFeatures.engine_hp).label('min_hp'),
            func.max(CarFeatures.engine_hp).label('max_hp')
        )
        .select_from(CarFeatures)
        .join(VehicleTypes, CarFeatures.vehicle_type_id == VehicleTypes.id)
        .group_by(VehicleTypes.id, VehicleTypes.name)
        .order_by(func.avg(CarFeatures.engine_hp).desc())
    )
    results = query.all()
    keys = query.statement.columns.keys()
    return [dict(zip(keys, row)) for row in results]


# мощность по году
def get_stat_by_year():
    query = (
        db.session.query(
            CarFeatures.year,
            func.round(cast(func.avg(CarFeatures.engine_hp), Numeric), 2).label('avg_hp'),
            func.min(CarFeatures.engine_hp).label('min_hp'),
            func.max(CarFeatures.engine_hp).label('max_hp')
        )
        .select_from(CarFeatures)
        .group_by(CarFeatures.year)
        .order_by(CarFeatures.year)
    )
    results = query.all()
    keys = query.statement.columns.keys()
    return [dict(zip(keys, row)) for row in results]
