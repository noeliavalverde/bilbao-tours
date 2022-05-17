from http import client
from urllib import response
from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.stops import TourStop, TourStopRepository


def test_should_return_empty_list_of_tour_stops():
    tour_stop_repository = TourStopRepository(temp_file())
    app = create_app(repositories={"tour_stops": tour_stop_repository})
    client = app.test_client()

    response = client.get("/api/tour-stops")

    assert response.json == []

def test_should_return_all_existing_tour_stops():
    tour_stop_repository = TourStopRepository(temp_file())
    app = create_app(repositories={"tour_stops": tour_stop_repository})
    client = app.test_client()

    tour_stop1 = TourStop(
        stop_id = "stop_001",
        stop_name = "Primera parada",
        stop_description = "Esta debe ser la descripción de la primera parada",
        before_picture = "esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente" 
    )
    tour_stop2 = TourStop(
        stop_id = "stop_002",
        stop_name = "Segunda parada",
        stop_description = "Esta debe ser la descripción de la segunda parada",
        before_picture = "esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente" 
    )

    tour_stop_repository.save_tour_stop(tour_stop1)
    tour_stop_repository.save_tour_stop(tour_stop2)

    response = client.get("api/tour-stops")

    assert response.json == [
        {
            "stop_id": "stop_001",
            "stop_name": "Primera parada",
            "stop_description": "Esta debe ser la descripción de la primera parada",
            "before_picture": "esto debe ser una url con imagen pasado",
            "after_picture": "esto debe ser una url con imagen presente" 
        },
        {
            "stop_id": "stop_002",
            "stop_name": "Segunda parada",
            "stop_description": "Esta debe ser la descripción de la segunda parada",
            "before_picture": "esto debe ser una url con imagen pasado",
            "after_picture": "esto debe ser una url con imagen presente" 
        }
    ]
