from app.extensions import ma, db
from app.models import TransmissionTypes

class TransmissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TransmissionTypes
        load_instance = True
        sqla_session = db.session

transmission_schema = TransmissionSchema()
transmissions_schema = TransmissionSchema(many=True)
