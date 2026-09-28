import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_get_students_returns_seeded_students(client):
    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Ava Johnson"


def test_get_student_returns_one_student(client):
    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json["email"] == "ava.johnson@example.com"


def test_get_missing_student_returns_not_found(client):
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json == {"error": "Student not found"}


def test_add_student_returns_created_student(client):
    response = client.post(
        "/students",
        json={
            "name": "Mia Patel",
            "email": "mia.patel@example.com",
            "course": "Data Science",
        },
    )

    assert response.status_code == 201
    assert response.json["id"] == 3
    assert response.json["name"] == "Mia Patel"


def test_add_student_rejects_missing_fields(client):
    response = client.post("/students", json={"name": "Incomplete Student"})

    assert response.status_code == 400
    assert "email" in response.json["missing_fields"]
    assert "course" in response.json["missing_fields"]


def test_add_student_rejects_invalid_email(client):
    response = client.post(
        "/students",
        json={"name": "Bad Email", "email": "invalid", "course": "Physics"},
    )

    assert response.status_code == 400
    assert response.json["error"] == "Email must be valid"
