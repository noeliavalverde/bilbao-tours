import sqlite3
from src.webserver import create_app
from src.domain.tour import TourRepository
from src.domain.user import UserRepository


database_path = "data/database.db"

repositories = {
    "tours": TourRepository(database_path),
    "users": UserRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
