from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.tour import Tour, TourRepository


def test_should_return_empty_list_of_tours():

    tour_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    response = client.get("/api/tours")

    assert response.json == []


def test_should_return_list_of_tours_without_stops():
    tour_repository = TourRepository(temp_file())
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
        tour_front_image="https://www.example.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["nature", "citylife"],
        stops=None,
    )

    tour_repository.save_tour(tour1)
    tour_repository.save_tour(tour2)

    response = client.get("/api/tours")

    assert response.json == [
        {
            "tour_id": "1",
            "tour_name": "Tour primero",
            "tour_desc": "Esto es una descripción para testear el tour primero",
            "tour_front_image": "https://www.bilbao.bi/bilbao.jpg",
            "favourite_tour": 0,
            "filters": ["arquitecture", "history", "monuments"],
            "stops": [],
        },
        {
            "tour_id": "2",
            "tour_name": "Tour segundo",
            "tour_desc": "Esto es una descripción para testear el tour segundo",
            "tour_front_image": "https://www.example.bi/bilbao.jpg",
            "favourite_tour": 0,
            "filters": ["nature", "citylife"],
            "stops": [],
        },
    ]
