import csv
from app import create_app
from app.models import Building, City, TypeBuilding, Country

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    