from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def test_should_return_empty_list_of_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_return_list_of_users():

    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    admin_1 = User(
        id="user-1",
        name="admin-1",
    )
    admin_2 = User(
        id="user-2",
        name="admin-2",
    )

    user_repository.save(admin_1)
    user_repository.save(admin_2)

    response = client.get("/api/users")

    assert response.json == [
        {
            "id": "user-1",
            "name": "admin-1",
        },
        {
            "id": "user-2",
            "name": "admin-2",
        },
    ]
