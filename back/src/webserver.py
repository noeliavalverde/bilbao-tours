from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/tours", methods=["GET"])
    def tours_get():
        all_tours = repositories["tours"].get_all_tours()
        return object_to_json(all_tours)

    @app.route("/api/tour-stops", methods=["GET"])
    def tour_stops_get():
        all_tour_stops = repositories["tours"].get_all_stops()
        return object_to_json(all_tour_stops)

    @app.route("/api/tours/<tour_id>", methods=["GET"])
    def tour_detail_get(tour_id):
        tour_detail = repositories["tours"].get_tour_by_id(tour_id)
        return object_to_json(tour_detail)

    @app.route("/api/users", methods=["GET"])
    def users_get_all():
        all_users = repositories["users"].get_all()
        return object_to_json(all_users)

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_by_id(body["user"])

        if user is None or (body["password"]) != user.password:
            return "", 401

        return user.to_dict(), 200

    @app.route("/api/tours/<tour_id>", methods=["DELETE"])
    def tour_delete(tour_id):
        tour_to_delete = repositories["tours"].delete_tour_by_id(tour_id)
        return ""

    return app
