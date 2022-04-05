from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.tour import Tour, TourRepository


def test_should_return_empty_list_of_tours():

    tour_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    response = client.get("/api/tours")

    assert response.json == []
