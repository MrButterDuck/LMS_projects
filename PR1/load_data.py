import csv
from app import create_app
from app.extensions import db
from app.models import CarMake, CarModel, CategoryTypes, MarketCategory, TransmissionTypes, DrivenWheelsTypes, VehicleTypes, CarFeatures
from app.crud import get_or_create, create
 
app = create_app()
 
 
def load(filepath):
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            make = get_or_create(CarMake, name=row['Make'])
            model = get_or_create(CarModel, name=row['Model'], make_id=make.id)
            transmission = get_or_create(TransmissionTypes, name=row['Transmission Type'])
            driven_wheels = get_or_create(DrivenWheelsTypes, name=row['Driven_Wheels'])
            vehicle_type = get_or_create(VehicleTypes, name=row['Vehicle Style'])
 
            doors_raw = row['Number of Doors'].strip()
            doors = int(float(doors_raw)) if doors_raw else None
 
            hp_raw = row['Engine HP'].strip()
            hp = float(hp_raw) if hp_raw else None
 
            cyl_raw = row['Engine Cylinders'].strip()
            cyl = int(float(cyl_raw)) if cyl_raw else None
 
            feature = CarFeatures(
                model_id=model.id,
                year=int(row['Year']),
                transmission_id=transmission.id,
                driven_wheels_id=driven_wheels.id,
                vehicle_type_id=vehicle_type.id,
                number_of_doors=doors,
                engine_cylinders=cyl,
                engine_hp=hp,
            )
            create(feature)
 
            categories_raw = row['Market Category'].strip()
            if categories_raw:
                for cat_name in categories_raw.split(','):
                    cat_name = cat_name.strip()
                    if cat_name:
                        category = get_or_create(CategoryTypes, name=cat_name)
                        mc = MarketCategory(category_id=category.id, model_id=model.id)
                        create(mc)
 
            if i % 500 == 0:
                print(f'Загружено строк: {i}')
 
    print('Выполнено')
 
 
if __name__ == '__main__':
    load('app\data\data.csv') 