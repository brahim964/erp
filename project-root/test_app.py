# tests/test_app.py
import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a la Gestoría de Automóviles' in response.data
