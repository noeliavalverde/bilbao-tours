import sqlite3
import json


class Tour:
    def __init__(
        self,
        tour_id,
        tour_name,
        tour_desc,
        tour_front_image,
        favourite_tour,
        filters,
        stops=None,
    ):
        self.tour_id = tour_id
        self.tour_name = tour_name
        self.tour_desc = tour_desc
        self.tour_front_image = tour_front_image
        self.favourite_tour = favourite_tour
        self.filters = filters
        self.stops = stops

    def to_dict(self):
        return {
            "tour_id": self.tour_id,
            "tour_name": self.tour_name,
            "tour_desc": self.tour_desc,
            "tour_front_image": self.tour_front_image,
            "favourite_tour": self.favourite_tour,
            "filters": self.filters,
            "stops": self.stops,
        }


class TourRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE if not exists tours (
                tour_id varchar PRIMARY KEY,
                tour_name text,
                tour_desc text,
                tour_front_image varchar,
                favourite_tour bool,
                filters varchar
                );

                CREATE TABLE if not exists prepared_tour (
                tour_id varchar,
                stop_id varchar,
                FOREIGN KEY (tour_id) REFERENCES tours(tour_id),
                FOREIGN KEY (stop_id) REFERENCES tour_stops(stop_id)
                )
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()

    def get_all_tours(self):
        sql = """SELECT * FROM tours"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        tours = []

        for item in data:
            tour = Tour(
                tour_id=item["tour_id"],
                tour_name=item["tour_name"],
                tour_desc=item["tour_desc"],
                tour_front_image=item["tour_front_image"],
                favourite_tour=item["favourite_tour"],
                filters=json.loads(item["filters"]),
            )
            tours.append(tour)

        return tours

    def save_tour(self, tour):
        sql = """INSERT into tours (tour_id,
                tour_name,
                tour_desc,
                tour_front_image,
                favourite_tour,
                filters) values (:tour_id, :tour_name, :tour_desc, :tour_front_image, :favourite_tour, :filters)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "tour_id": tour.tour_id,
                "tour_name": tour.tour_name,
                "tour_desc": tour.tour_desc,
                "tour_front_image": tour.tour_front_image,
                "favourite_tour": tour.favourite_tour,
                "filters": json.dumps(tour.filters),
            },
        )
        conn.commit()
