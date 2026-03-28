from app.extensions import ma, db
from app.models import CarModel
from app.schemas.car_features_schema import CarFeaturesSchema
from app.schemas.market_category_schema import MarketCategorySchema
from app.schemas.car_make_schema import CarMakeSchema

class CarModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarModel
        load_instance = True
        sqla_session = db.session

    make_id = ma.auto_field()
    make = ma.Nested(CarMakeSchema())
    features = ma.Nested(CarFeaturesSchema(many=True))
    market_categories = ma.Nested(MarketCategorySchema(many=True))

car_model_schema = CarModelSchema()
car_models_schema = CarModelSchema(many=True)
