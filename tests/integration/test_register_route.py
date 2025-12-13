import pytest
from app import create_app
from app.database.db import db

@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_registration_route_success(client):
    """
    Test /auth/register route with valid inputs.
    """
    payload = {
        "email": "test@example.com",
        "password": "Test1234"
    }

    response = client.post("/auth/register/", json=payload)
    assert response.status_code == 201
    assert response.json["message"] == "Registration successful. Confirmation email sent."

def test_registration_route_existing_email(client):
    """
    Test /auth/register route where email already exists.
    """
    payload = {
        "email": "test@example.com",
        "password": "Test1234"
    }

    # Simulate existing email
    client.post("/auth/register/", json=payload)
    response = client.post("/auth/register/", json=payload)
    assert response.status_code == 409
    assert "Email address is already registered." in response.json["error"]

def test_registration_route_invalid_email(client):
    """
    Test /auth/register route with invalid email.
    """
    payload = {
        "email": "notanemail",
        "password": "Test1234"
    }

    response = client.post("/auth/register/", json=payload)
    assert response.status_code == 400
    assert "Invalid email format." in response.json["error"]

def test_registration_route_weak_password(client):
    """
    Test /auth/register route with weak password.
    """
    payload = {
        "email": "test@example.com",
        "password": "123"
    }

    response = client.post("/auth/register/", json=payload)
    assert response.status_code == 400
    assert "Password must be at least 8 characters long." in response.json["error"]