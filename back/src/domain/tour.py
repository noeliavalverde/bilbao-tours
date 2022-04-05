import sqlite3


class Tour:
    def __init__(self):
        pass


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
                tour_id varchar,
                tour_name text,
                tour_desc text,
                favorite_tour numeric,
                completed numeric,
                filters numeric,
                quarter numeric
                )
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_tours(self):
        sql = """SELECT * FROM tours"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        tours = []

        for item in data:
            tour = Tour(**item)

            tours.append(tour)

        return tours
