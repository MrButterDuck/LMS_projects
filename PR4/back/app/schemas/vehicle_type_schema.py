from app.extensions import ma, db
from app.models import VehicleTypes

class VehicleTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VehicleTypes
        load_instance = True
        sqla_session = db.session

vehicle_type_schema = VehicleTypeSchema()
vehicle_types_schema = VehicleTypeSchema(many=True)
