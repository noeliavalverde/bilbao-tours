import sqlite3
from src.webserver import create_app
from src.domain.tour import TourRepository


database_path = "data/database.db"

repositories = {
    "tours": TourRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
