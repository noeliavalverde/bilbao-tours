from src.lib.utils import temp_file
from src.webserver import create_app

# from src.domain.stops import TourStop, TourStopRepository
from src.domain.tour import Tour, TourRepository, TourStop


def test_should_return_tour_by_id_without_stops():
    tour_repository = TourRepository(temp_file())
    tour_stop_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    tour1 = Tour(
        tour_id="1",
        tour_name="Tour primero",
        tour_desc="Esto es una descripción para testear el tour primero",
        tour_front_image="https://www.bilbao.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["arquitecture", "history", "monuments"],
        stops=None,
    )
    tour2 = Tour(
        tour_id="2",
        tour_name="Tour segundo",
        tour_desc="Esto es una descripción para testear el tour segundo",
        tour_front_image="https://www.bilbao.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["arquitecture", "history", "monuments"],
        stops=None,
    )

    tour_repository.save_tour(tour1)
    tour_repository.save_tour(tour2)

    tour_stop1 = TourStop(
        stop_id="stop_001",
        stop_name="Primera parada",
        stop_description="Esta debe ser la descripción de la primera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )
    tour_stop2 = TourStop(
        stop_id="stop_002",
        stop_name="Segunda parada",
        stop_description="Esta debe ser la descripción de la segunda parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_repository.save_tour_stop(tour_stop1)
    tour_repository.save_tour_stop(tour_stop2)

    response = client.get("/api/tours/1")

    assert response.json == {
        "tour_id": "1",
        "tour_name": "Tour primero",
        "tour_desc": "Esto es una descripción para testear el tour primero",
        "tour_front_image": "https://www.bilbao.bi/bilbao.jpg",
        "favourite_tour": 0,
        "filters": ["arquitecture", "history", "monuments"],
        "stops": [],
    }


def test_should_return_tour_by_id_with_stops():
    tour_repository = TourRepository(temp_file())
    tour_stop_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    tour1 = Tour(
        tour_id="1",
        tour_name="Tour primero",
        tour_desc="Esto es una descripción para testear el tour primero",
        tour_front_image="https://www.bilbao.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["arquitecture", "history", "monuments"],
        stops=[
            {
                "stop_id": "stop_001",
                "stop_name": "Primera parada",
                "stop_description": "Esta debe ser la descripción de la primera parada",
                "before_picture": "esto debe ser una url con imagen pasado",
                "after_picture": "esto debe ser una url con imagen presente",
            },
            {
                "stop_id": "stop_00",
                "stop_name": "Tercera parada",
                "stop_description": "Esta debe ser la descripción de la tercera parada",
                "before_picture": "esto debe ser una url con imagen pasado",
                "after_picture": "esto debe ser una url con imagen presente",
            },
        ],
    )

    tour_repository.save_tour(tour1)

    tour_stop1 = TourStop(
        stop_id="stop_001",
        stop_name="Primera parada",
        stop_description="Esta debe ser la descripción de la primera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )
    tour_stop2 = TourStop(
        stop_id="stop_002",
        stop_name="Segunda parada",
        stop_description="Esta debe ser la descripción de la segunda parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )
    tour_stop3 = TourStop(
        stop_id="stop_003",
        stop_name="Tercera parada",
        stop_description="Esta debe ser la descripción de la tercera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_repository.save_tour_stop(tour_stop1)
    tour_repository.save_tour_stop(tour_stop2)
    tour_repository.save_tour_stop(tour_stop3)
    tour_repository.save_tour_stops_to_tour("1", ["stop_001", "stop_002"])

    response = client.get("/api/tours/1")

    assert response.json == {
        "tour_id": "1",
        "tour_name": "Tour primero",
        "tour_desc": "Esto es una descripción para testear el tour primero",
        "tour_front_image": "https://www.bilbao.bi/bilbao.jpg",
        "favourite_tour": 0,
        "filters": ["arquitecture", "history", "monuments"],
        "stops": [
            {
                "stop_id": "stop_001",
                "stop_name": "Primera parada",
                "stop_description": "Esta debe ser la descripción de la primera parada",
                "before_picture": "esto debe ser una url con imagen pasado",
                "after_picture": "esto debe ser una url con imagen presente",
            },
            {
                "stop_id": "stop_002",
                "stop_name": "Segunda parada",
                "stop_description": "Esta debe ser la descripción de la segunda parada",
                "before_picture": "esto debe ser una url con imagen pasado",
                "after_picture": "esto debe ser una url con imagen presente",
            },
        ],
    }
