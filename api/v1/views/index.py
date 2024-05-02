# from flask import Flask, jsonify
# from models import storage

# app = Flask(__name__)


# @app.route('/api/v1/stats', methods=['GET'])
# def get_stats():
#     counts = {
#         "amenities": storage.count("Amenity"),
#         "cities": storage.count("City"),
#         "places": storage.count("Place"),
#         "reviews": storage.count("Review"),
#         "states": storage.count("State"),
#         "users": storage.count("User")
#     }
#     return jsonify(counts)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


#!/usr/bin/python3
"""module index.py"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns json status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    stats_dict = {}
    for key, value in classes.items():
        stats_dict[key] = storage.count(value)
    return jsonify(stats_dict)
