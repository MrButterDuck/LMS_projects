import csv
from app import create_app
from app.models import Country, City, Building, TypeBuilding
from app.crud import create

app = create_app()

def load_csv(filepath, model_func):
    with open(filepath, encoding='windows-1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            create(model_func(row))


if __name__ == '__main__':
    # load_csv('app/data/country.csv', lambda r: Country(r['name']))
    # load_csv('app/data/city.csv',    lambda r: City(r['name'], int(r['id'])))
    # load_csv('app/data/building.csv', lambda r: Building(r['name'], int(r['id1']),int(r['id2']), int(r['year']), float(r['height'])))

    app.run(debug=True, use_reloader=False)
    