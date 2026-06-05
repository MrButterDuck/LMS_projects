from app.extensions import ma, db
from app.models import CarMake

class CarMakeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarMake
        load_instance = True
        sqla_session = db.session

car_make_schema = CarMakeSchema()
car_makes_schema = CarMakeSchema(many=True)

