import pytest

from app import create_app, db
from app.models import Habit


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()

        yield app.test_client()

        db.session.remove()
        db.drop_all()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_habit(client):
    response = client.post(
        "/add",
        data={
            "name": "Reading",
            "description": "Read books",
            "target_per_day": 2
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Reading" in response.data


def test_search_habit(client):
    client.post(
        "/add",
        data={
            "name": "Workout",
            "description": "Gym",
            "target_per_day": 1
        }
    )

    response = client.get("/search?q=Workout")

    assert response.status_code == 200
    assert b"Workout" in response.data