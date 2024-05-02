# #!/usr/bin/python3
# """cities.py"""

# from api.v1.views import app_views
# from flask import abort, jsonify, make_response, request
# from models import storage
# from models.city import City
# from models.state import State


# @app_views.route('/states/<string:state_id>/cities', methods=['GET'],
#                  strict_slashes=False)
# def get_cities(state_id):
#     """get city information for all cities in a specified state"""
#     state = storage.get("State", state_id)
#     if state is None:
#         abort(404)
#     cities = []
#     for city in state.cities:
#         cities.append(city.to_dict())
#     return jsonify(cities)


# @app_views.route('/cities/<string:city_id>', methods=['GET'],
#                  strict_slashes=False)
# def get_city(city_id):
#     """get city information for specified city"""
#     city = storage.get("City", city_id)
#     if city is None:
#         abort(404)
#     return jsonify(city.to_dict())


# @app_views.route('/cities/<string:city_id>', methods=['DELETE'],
#                  strict_slashes=False)
# def delete_city(city_id):
#     """deletes a city based on its city_id"""
#     city = storage.get("City", city_id)
#     if city is None:
#         abort(404)
#     city.delete()
#     storage.save()
#     return (jsonify({}))


# @app_views.route('/states/<string:state_id>/cities/', methods=['POST'],
#                  strict_slashes=False)
# def post_city(state_id):
#     """create a new city"""
#     state = storage.get("State", state_id)
#     if state is None:
#         abort(404)
#     if not request.get_json():
#         return make_response(jsonify({'error': 'Not a JSON'}), 400)
#     if 'name' not in request.get_json():
#         return make_response(jsonify({'error': 'Missing name'}), 400)
#     kwargs = request.get_json()
#     kwargs['state_id'] = state_id
#     city = City(**kwargs)
#     city.save()
#     return make_response(jsonify(city.to_dict()), 201)


# @app_views.route('/cities/<string:city_id>', methods=['PUT'],
#                  strict_slashes=False)
# def put_city(city_id):
#     """update a city"""
#     city = storage.get("City", city_id)
#     if city is None:
#         abort(404)
#     if not request.get_json():
#         return make_response(jsonify({'error': 'Not a JSON'}), 400)
#     for attr, val in request.get_json().items():
#         if attr not in ['id', 'state_id', 'created_at', 'updated_at']:
#             setattr(city, attr, val)
#     city.save()
#     return jsonify(city.to_dict())


#!/usr/bin/python3
"""handles all default RESTFul API actions"""
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """returns all cities"""
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """returns city by id"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        return abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """deletes city by id"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    """creates a new city"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    if not request.get_json():
        return abort(400, 'Not a JSON')
    city_data = request.get_json()
    if 'name' not in city_data:
        return abort(400, 'Missing name')
    city_data['state_id'] = state_id
    city = City(**city_data)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_city(city_id):
    """updates a city by id"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    city = storage.get(City, city_id)
    if city:
        if not request.get_json():
            return abort(400, 'Not a JSON')
        data = request.get_json()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at', 'state_id']:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        return abort(404)
