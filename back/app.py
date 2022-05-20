import sqlite3
from src.webserver import create_app
from src.domain.tour import TourRepository
from src.domain.stops import TourStopRepository


database_path = "data/database.db"

repositories = {
    "tours": TourRepository(database_path),
    "tour_stops": TourStopRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
