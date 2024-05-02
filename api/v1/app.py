#!/usr/bin/python3
"""app module to create API"""
import os

from flask import Blueprint, Flask, jsonify, make_response
from flask_cors import CORS

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exc):
    """calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """error handler"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')), threaded=True)
