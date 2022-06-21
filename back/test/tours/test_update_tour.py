from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.tour import TourRepository, Tour


def test_should_update_tour():

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

    body = {
        "tour_id": "tour_1",
        "tour_name": "CHANGED Tour primero",
        "tour_desc": " CHANGED Esto es una descripción para testear el tour primero",
        "tour_front_image": "https://www.bilbao.bi/bilbao.jpg",
        "favourite_tour": 0,
        "filters": ["arquitecture", "history", "monuments"],
        "stops": [],
    }

    response = client.put("/api/tours/tour_1", json=body)

    assert response.status_code == 200

    response_get = client.get("/api/tours/tour_1")

    assert response_get.json == {
        "tour_id": "tour_1",
        "tour_name": "CHANGED Tour primero",
        "tour_desc": " CHANGED Esto es una descripción para testear el tour primero",
        "tour_front_image": "https://www.bilbao.bi/bilbao.jpg",
        "favourite_tour": 0,
        "filters": ["arquitecture", "history", "monuments"],
        "stops": [],
    }
