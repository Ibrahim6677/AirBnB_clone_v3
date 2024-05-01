from flask import Flask, jsonify
from models import storage

app = Flask(__name__)


@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(counts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
