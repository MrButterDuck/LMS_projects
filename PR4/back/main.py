import csv
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    
# curl http://127.0.0.1:5000/api/v1/car-models/
# curl http://127.0.0.1:5000/api/v1/car-models/3
# curl -u student:dvfu -i -H "Content-Type:application/json" --data "{\"make\":\"Toyota\",\"model\":\"Hilux Surf\",\"year\":1996,\"engine_hp\":150,\"engine_cylinders\":4,\"transmission\":\"MANUAL\",\"driven_wheels\":\"rear wheel drive\",\"number_of_doors\":4,\"market_categories\":\"Luxury,High-Performance\",\"vehicle_type\":\"JEEP\"}" http://127.0.0.1:5000/api/v1/car-models/
# curl -u student:dvfu -i -X PUT -H "Content-Type:application/json" --data "{\"make\":\"Toyota\",\"model\":\"Hilux Surf\",\"year\":2001,\"engine_hp\":150,\"engine_cylinders\":4,\"transmission\":\"MANUAL\",\"driven_wheels\":\"all wheel drive\",\"number_of_doors\":4,\"market_categories\":\"Performance,High-Performance\",\"vehicle_type\":\"JEEP\"}" http://127.0.0.1:5000/api/v1/car-models/85
# curl -u student:dvfu -i -X DELETE http://127.0.0.1:5000/api/v1/car-models/84

# curl http://127.0.0.1:5000/api/v1/aggregate/all/
# curl http://127.0.0.1:5000/api/v1/aggregate/make/
# curl http://127.0.0.1:5000/api/v1/aggregate/transmission/
# curl http://127.0.0.1:5000/api/v1/aggregate/vehicle-type/
# curl http://127.0.0.1:5000/api/v1/aggregate/year/