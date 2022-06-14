from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.tour import Tour, TourRepository, TourStop


def test_should_delete_one_tour_without_stops_by_id():
    tour_repository = TourRepository(temp_file())
    tour_stop_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    tour1 = Tour(
        tour_id="tour1",
        tour_name="Tour primero",
        tour_desc="Esto es una descripción para testear el tour primero",
        tour_front_image="https://www.bilbao.bi/bilbao.jpg",
        favourite_tour=0,
        filters=["arquitecture", "history", "monuments"],
        stops=[],
    )

    tour_repository.save_tour(tour1)

    response = client.delete("api/tours/tour1")

    assert response.status_code == 200
