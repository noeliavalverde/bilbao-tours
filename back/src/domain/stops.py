# import sqlite3
# import json

# class TourStop:
#     def __init__(self, stop_id, stop_name, stop_description, before_picture, after_picture):
#         self.stop_id = stop_id
#         self.stop_name = stop_name
#         self.stop_description = stop_description
#         self.before_picture = before_picture
#         self.after_picture = after_picture

#     def to_dict(self):
#         return  {
#             "stop_id": self.stop_id,
#             "stop_name": self.stop_name,
#             "stop_description": self.stop_description,
#             "before_picture": self.before_picture,
#             "after_picture": self.after_picture,
#         }

# class TourStopRepository:
#     def __init__(self, database_path):
#         self.database_path = database_path
#         self.init_tables()

#     def create_conn(self):
#         conn = sqlite3.connect(self.database_path)
#         conn.row_factory = sqlite3.Row
#         return conn

#     def init_tables(self):
#         sql = """
#                 CREATE TABLE if not exists tour_stops (
#                 stop_id varchar PRIMARY KEY,
#                 stop_name varchar,
#                 stop_description varchar,
#                 before_picture varchar,
#                 after_picture varchar
#                 )
#                 """

#         conn = self.create_conn()
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         conn.commit()

#     def get_all_stops(self):
#         sql = """ SELECT * FROM tour_stops """
#         conn = self.create_conn()
#         cursor = conn.cursor()
#         cursor.execute(sql)

#         data = cursor.fetchall()

#         tour_stops = []

#         for item in data:
#             tour_stop = TourStop(**item)
#             tour_stops.append(tour_stop)
#         return tour_stops

#     def save_tour_stop(self, tour_stop):
#         sql = """
#                 INSERT into tour_stops
#                 (stop_id,
#                 stop_name,
#                 stop_description,
#                 before_picture,
#                 after_picture) values (:stop_id, :stop_name, :stop_description, :before_picture, :after_picture)
#                 """
#         conn = self.create_conn()
#         cursor = conn.cursor()
#         cursor.execute(
#             sql,
#             tour_stop.to_dict(),
#         )
#         conn.commit()
