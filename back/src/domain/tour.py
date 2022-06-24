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
            "stops": self.stops if self.stops else [],
        }


class TourStop:
    def __init__(
        self,
        stop_id,
        stop_name,
        stop_description,
        before_picture,
        before_figcaption,
        before_alt_text,
        after_picture,
        after_figcaption,
        after_alt_text,
    ):

        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_description = stop_description
        self.before_picture = before_picture
        self.before_figcaption = before_figcaption
        self.before_alt_text = before_alt_text
        self.after_picture = after_picture
        self.after_figcaption = after_figcaption
        self.after_alt_text = after_alt_text

    def to_dict(self):
        return {
            "stop_id": self.stop_id,
            "stop_name": self.stop_name,
            "stop_description": self.stop_description,
            "before_picture": self.before_picture,
            "before_figcaption": self.before_figcaption,
            "before_alt_text": self.before_alt_text,
            "after_picture": self.after_picture,
            "after_figcaption": self.after_figcaption,
            "after_alt_text": self.after_alt_text,
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
                FOREIGN KEY ("tour_id") REFERENCES "tours"("tour_id"),
                FOREIGN KEY ("stop_id") REFERENCES "tour_stops"("stop_id")
                );

                CREATE TABLE if not exists tour_stops (
                stop_id varchar PRIMARY KEY,
                stop_name varchar,
                stop_description varchar,
                before_picture varchar,
                before_figcaption varchar,
                before_alt_text,
                after_picture varchar,
                after_figcaption varchar,
                after_alt_text
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
                stops=self.get_stops_by_tour_id(item["tour_id"]),
            )
            tours.append(tour)

        return tours

    def save_tour(self, tour):
        sql = """INSERT OR REPLACE into tours (tour_id,
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

    def get_tour_by_id(self, tour_id):
        sql = """SELECT * FROM tours WHERE tour_id=:tour_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"tour_id": tour_id})
        data = cursor.fetchone()
        tour = Tour(
            tour_id=data["tour_id"],
            tour_name=data["tour_name"],
            tour_desc=data["tour_desc"],
            tour_front_image=data["tour_front_image"],
            favourite_tour=data["favourite_tour"],
            filters=json.loads(data["filters"]),
            stops=self.get_stops_by_tour_id(tour_id),
        )

        return tour

    def get_stop_by_id(self, stop_id):
        sql = """SELECT * FROM tour_stops WHERE stop_id=:stop_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"stop_id": stop_id})
        data = cursor.fetchone()
        stop = TourStop(
            stop_id=data["stop_id"],
            stop_name=data["stop_name"],
            stop_description=data["stop_description"],
            before_picture=data["before_picture"],
            before_figcaption=data["before_figcaption"],
            before_alt_text=data["before_alt_text"],
            after_picture=data["after_picture"],
            after_figcaption=data["after_figcaption"],
            after_alt_text=data["after_alt_text"],
        )

        return stop

    def save_tour_stops_to_tour(self, tour_id, stops):
        sql = """
        DELETE from prepared_tour WHERE tour_id = :tour_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"tour_id": tour_id},
        )
        conn.commit()
        sql_prepared_tour = """INSERT INTO prepared_tour (tour_id, stop_id) VALUES (:tour_id, :stop_id)"""

        for stop in stops:
            cursor.execute(sql_prepared_tour, {"tour_id": tour_id, "stop_id": stop})
        conn.commit()
        conn.close()

    def get_stops_by_tour_id(self, tour_id):

        conn = self.create_conn()
        cursor = conn.cursor()
        sql = """SELECT tour_stops.stop_id,
                        tour_stops.stop_name, 
                        tour_stops.stop_description, 
                        tour_stops.before_picture, 
                        tour_stops.before_figcaption, 
                        tour_stops.before_alt_text, 
                        tour_stops.after_picture, 
                        tour_stops.after_figcaption, 
                        tour_stops.after_alt_text
                FROM prepared_tour
                INNER JOIN tours USING (tour_id)
                INNER JOIN tour_stops USING (stop_id)
                WHERE tour_id = :tour_id
            """
        cursor.execute(sql, {"tour_id": tour_id})
        stops = cursor.fetchall()
        stops_list = []

        for stop in stops:

            tour_stop = TourStop(
                stop_id=stop["stop_id"],
                stop_name=stop["stop_name"],
                stop_description=stop["stop_description"],
                before_picture=stop["before_picture"],
                before_figcaption=stop["before_figcaption"],
                before_alt_text=stop["before_alt_text"],
                after_picture=stop["after_picture"],
                after_figcaption=stop["after_figcaption"],
                after_alt_text=stop["after_alt_text"],
            )

            stop_dict = tour_stop.to_dict()
            stops_list.append(stop_dict)

        conn.close()
        return stops_list

    def get_all_stops(self):
        sql = """ SELECT * FROM tour_stops """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        tour_stops = []

        for item in data:
            tour_stop = TourStop(**item)
            tour_stops.append(tour_stop)
        return tour_stops

    def save_tour_stop(self, tour_stop):
        sql = """
                INSERT into tour_stops
                (stop_id,
                stop_name,
                stop_description,
                before_picture,
                before_figcaption,
                before_alt_text,
                after_picture,
                after_figcaption,
                after_alt_text) values (:stop_id, 
                                        :stop_name, 
                                        :stop_description, 
                                        :before_picture, 
                                        :before_figcaption, 
                                        :before_alt_text,
                                        :after_picture, 
                                        :after_figcaption,
                                        :after_alt_text)
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            tour_stop.to_dict(),
        )
        conn.commit()

    def delete_tour_by_id(self, tour_id):
        sql = """
                DELETE FROM tours
                WHERE tours.tour_id = :tour_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"tour_id": tour_id})
        conn.commit()
        conn.close()
        return ""

    def delete_stop_by_id(self, stop_id):
        sql = """
                DELETE FROM tour_stops
                WHERE tour_stops.stop_id = :stop_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"stop_id": stop_id})
        conn.commit()
        conn.close()
        return ""
