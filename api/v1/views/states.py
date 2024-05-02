# #!/usr/bin/python3
# """states.py"""

# from flask import abort, jsonify, make_response, request

# from api.v1.views import app_views
# from models import storage
# from models.state import State


# @app_views.route('/states', methods=['GET'], strict_slashes=False)
# def get_states():
#     """get state information for all states"""
#     states = []
#     for state in storage.all("State").values():
#         states.append(state.to_dict())
#     return jsonify(states)


# @app_views.route('/states/<string:state_id>', methods=['GET'],
#                  strict_slashes=False)
# def get_state(state_id):
#     """get state information for specified state"""
#     state = storage.get("State", state_id)
#     if state is None:
#         abort(404)
#     return jsonify(state.to_dict())


# @app_views.route('/states/<string:state_id>', methods=['DELETE'],
#                  strict_slashes=False)
# def delete_state(state_id):
#     """deletes a state based on its state_id"""
#     state = storage.get("State", state_id)
#     if state is None:
#         abort(404)
#     state.delete()
#     storage.save()
#     return (jsonify({}))


# @app_views.route('/states/', methods=['POST'], strict_slashes=False)
# def post_state():
#     """create a new state"""
#     if not request.get_json():
#         return make_response(jsonify({'error': 'Not a JSON'}), 400)
#     if 'name' not in request.get_json():
#         return make_response(jsonify({'error': 'Missing name'}), 400)
#     state = State(**request.get_json())
#     state.save()
#     return make_response(jsonify(state.to_dict()), 201)


# @app_views.route('/states/<string:state_id>', methods=['PUT'],
#                  strict_slashes=False)
# def put_state(state_id):
#     """update a state"""
#     state = storage.get("State", state_id)
#     if state is None:
#         abort(404)
#     if not request.get_json():
#         return make_response(jsonify({'error': 'Not a JSON'}), 400)
#     for attr, val in request.get_json().items():
#         if attr not in ['id', 'created_at', 'updated_at']:
#             setattr(state, attr, val)
#     state.save()
#     return jsonify(state.to_dict())


#!/usr/bin/python3
"""handles all default RESTFul API actions"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states', strict_slashes=False)
def get_states():
    """returns all states"""
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """returns state by id"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """deletes state by id"""
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def post_state():
    """creates a new state"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    kwargs = request.get_json()
    if 'name' not in kwargs:
        abort(400, 'Missing name')
    state = State(**kwargs)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """updates a state by id"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    state = storage.get(State, state_id)
    if state:
        if not request.get_json():
            return abort(400, 'Not a JSON')
        data = request.get_json()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200
    else:
        abort(404)
