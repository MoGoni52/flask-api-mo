from flask_cors import CORS
from flask import Flask, jsonify, request
from controllers import cars
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': "Weclome to the Car API!"}), 200

@app.route('/cars', methods = ["GET", 'POST'])
def car():
    fns = {
        "GET": cars.index,
        "POST": cars.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/cars/<int:car_id>', methods = ['GET', 'PUT', 'DELETE'])
def car_handler(car_id):
    fns = {
        'GET': cars.show,
        'PUT': cars.update,
        'DELETE': cars.destroy
    }
    resp, code = fns[request.method](request, car_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({'message':f"Oops... {err}"}), 404

if __name__ == "__main__":
    app.run(debug=True)

