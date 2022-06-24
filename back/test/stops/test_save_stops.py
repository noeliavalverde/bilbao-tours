from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.tour import TourRepository, TourStop


def test_should_save_stop():

    tour_repository = TourRepository(temp_file())
    app = create_app(repositories={"tours": tour_repository})
    client = app.test_client()

    body = {
        "stop_id": "stop_001",
        "stop_name": "Primera parada",
        "stop_description": "Esta debe ser la descripción de la primera parada",
        "before_picture": "esto debe ser una url con imagen pasado",
        "before_figcaption": "Figcaption foto antigua",
        "before_alt_text": "alt text foto antigua",
        "after_picture": "esto debe ser una url con imagen presente",
        "after_figcaption": "figcaption actual - actual",
        "after_alt_text": "text alt actual",
    }

    response = client.post("/api/tour-stops", json=body)

    assert response.status_code == 200

    response_get = client.get("/api/tour-stops/stop_001")

    assert response_get.json == {
        "stop_id": "stop_001",
        "stop_name": "Primera parada",
        "stop_description": "Esta debe ser la descripción de la primera parada",
        "before_picture": "esto debe ser una url con imagen pasado",
        "before_figcaption": "Figcaption foto antigua",
        "before_alt_text": "alt text foto antigua",
        "after_picture": "esto debe ser una url con imagen presente",
        "after_figcaption": "figcaption actual - actual",
        "after_alt_text": "text alt actual",
    }
