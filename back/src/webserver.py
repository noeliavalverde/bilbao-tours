from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/tours", methods=["GET"])
    def tours_get():
        all_tours = repositories["tours"].get_all_tours()
        return object_to_json(all_tours)

    @app.route("/api/tour-stops", methods=["GET"])
    def tour_stops_get():
        all_tour_stops = repositories["tour_stops"].get_all_stops()
        return object_to_json(all_tour_stops)

    return app
