from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.tour import TourRepository, Tour, TourStop


def test_should_save_tour():

    tour_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    tour1 = Tour(
        tour_id="tour_1",
        tour_name="Tour primero",
        tour_desc="Esto es una descripción para testear el tour primero",
        tour_front_image="https://www.bilbao.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["arquitecture", "history", "monuments"],
        stops=None,
    )
    tour_repository.save_tour(tour1)
    tour_stop1 = TourStop(
        stop_id="stop_001",
        stop_name="Primera parada",
        stop_description="Esta debe ser la descripción de la primera parada",
        before_picture="esto debe ser una url con imagen pasado",
        before_figcaption="Figcaption foto antigua",
        before_alt_text="alt text foto antigua",
        after_picture="esto debe ser una url con imagen presente",
        after_figcaption="figcaption actual - actual",
        after_alt_text="text alt actual",
    )
    tour_stop2 = TourStop(
        stop_id="stop_002",
        stop_name="Segunda parada",
        stop_description="Esta debe ser la descripción de la segunda parada",
        before_picture="esto debe ser una url con imagen pasado",
        before_figcaption="Figcaption foto antigua",
        before_alt_text="alt text foto antigua",
        after_picture="esto debe ser una url con imagen presente",
        after_figcaption="figcaption actual - actual",
        after_alt_text="text alt actual",
    )

    tour_repository.save_tour_stop(tour_stop1)
    tour_repository.save_tour_stop(tour_stop2)

    body = {"tour_id": "tour_1", "stops": ["stop_001", "stop_002"]}

    response = client.post("/api/add-stops/tour_1", json=body)

    assert response.status_code == 200

    response_get = client.get("/api/tours/tour_1")

    assert response_get.json == {
        "tour_id": "tour_1",
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
                "before_figcaption": "Figcaption foto antigua",
                "before_alt_text": "alt text foto antigua",
                "after_picture": "esto debe ser una url con imagen presente",
                "after_figcaption": "figcaption actual - actual",
                "after_alt_text": "text alt actual",
            },
            {
                "stop_id": "stop_002",
                "stop_name": "Segunda parada",
                "stop_description": "Esta debe ser la descripción de la segunda parada",
                "before_picture": "esto debe ser una url con imagen pasado",
                "before_figcaption": "Figcaption foto antigua",
                "before_alt_text": "alt text foto antigua",
                "after_picture": "esto debe ser una url con imagen presente",
                "after_figcaption": "figcaption actual - actual",
                "after_alt_text": "text alt actual",
            },
        ],
    }
