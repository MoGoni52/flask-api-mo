from werkzeug import exceptions

cars = [
    {'id': 1, 'brand': 'Vauxhall', 'model': 'Corsa', 'year': 2017},
    {'id': 2, 'brand': 'Volkswaggon', 'model': 'Golf', 'year': 2015},
    {'id': 3, 'brand': 'Honda', 'model': 'Civic', 'year': 2020},
    {'id': 4, 'brand': 'Audi', 'model': 'A4', 'year': 2012}
]

def index(req):
    return [c for c in cars], 200

def create(req):
    new_car = req.get_json()
    new_car['id'] = sorted([c['id'] for c in cars])[-1] + 1
    cars.append(new_car)
    return new_car, 201

def show(req, uid):
    return find_by_uid(uid), 200

def update(req, uid):
    car = find_by_uid(uid)
    data = req.get_json()
    for key, val in data.items():
        car[key] = val
    return car, 200

def destroy(req, uid):
    car = find_by_uid(uid)
    cars.remove(car)
    return car, 204

def find_by_uid(uid):
    try:
        return next(c for c in cars if c['id'] == uid)
    except:
        raise exceptions.NotFound(f"We don't a car with {uid} id!")
