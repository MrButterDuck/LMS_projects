from app.extensions import ma, db
from app.models import DrivenWheelsTypes

class DrivenWheelsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DrivenWheelsTypes
        load_instance = True
        sqla_session = db.session

driven_wheels_schema = DrivenWheelsSchema()
driven_wheels_list_schema = DrivenWheelsSchema(many=True)
