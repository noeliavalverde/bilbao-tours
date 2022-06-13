from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    admin_1 = User(id="user-1", name="admin-1", password="12345")
    user_repository.save(admin_1)

    return client


def test_should_validate_login():
    client = setup()

    body = {"user": "user-1", "password": "12345"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 200
    assert response.json == {"id": "user-1", "name": "admin-1"}


def test_should_fail_if_invalid_password():
    client = setup()

    body = {"user": "user-1", "password": "wrong-password"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401


def test_should_fail_if_user_not_exists():
    client = setup()

    body = {"user": "wrong-user", "password": "wrong-password"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401
