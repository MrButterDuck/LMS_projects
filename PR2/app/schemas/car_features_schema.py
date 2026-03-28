from app.extensions import ma, db
from marshmallow import fields
from app.models import CarFeatures
from app.schemas.transmission_schema import TransmissionSchema
from app.schemas.driven_wheels_schema import DrivenWheelsSchema
from app.schemas.vehicle_type_schema import VehicleTypeSchema

class CarFeaturesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarFeatures
        load_instance = True
        sqla_session = db.session
    
    model_id = ma.auto_field()
    transmission_id = ma.auto_field()
    driven_wheels_id = ma.auto_field()
    vehicle_type_id = ma.auto_field()
    transmission = ma.Nested(TransmissionSchema())
    driven_wheels = ma.Nested(DrivenWheelsSchema())
    vehicle_type = ma.Nested(VehicleTypeSchema())

car_features_schema = CarFeaturesSchema()
car_features_list_schema = CarFeaturesSchema(many=True)

