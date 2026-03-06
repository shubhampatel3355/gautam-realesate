from fastapi.testclient import TestClient
from main import app
from database import Base, engine, SessionLocal
import models
import pytest

client = TestClient(app)

# Test db setup and teardown
def setup_module(module):
    models.Base.metadata.create_all(bind=engine)

def teardown_module(module):
    models.Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_property():
    response = client.post(
        "/properties/",
        json={
            "title": "Test Property",
            "price": "1000000",
            "category": "Villa",
            "key_features": [{"title": "Bedrooms", "value": "4"}],
            "description": "A beautiful test villa.",
            "property_for": "Sale",
            "sqft": "4000",
            "address": "123 Test St",
            "city": "Testville",
            "zip_code": "12345",
            "map_url": "",
            "media_files": [{"url": "http://example.com/image.jpg"}],
            "owner_name": "Test Owner",
            "contact_number": "555-1234",
            "amenities": ["Pool", "Gym"],
            "dynamic_fields": {"year_built": "2020"}
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Property"
    assert data["price"] == "1000000"
    assert "id" in data


def test_get_properties():
    response = client.get("/properties/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_property():
    # first get properties to find an ID
    res = client.get("/properties/")
    prop_id = res.json()[0]["id"]
    
    response = client.get(f"/properties/{prop_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == prop_id

def test_update_property():
    res = client.get("/properties/")
    prop_id = res.json()[0]["id"]
    prop_data = res.json()[0]
    
    prop_data["title"] = "Updated Test Property"
    
    response = client.put(f"/properties/{prop_id}", json=prop_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Test Property"


def test_resolve_url():
    # test the backend utility resolves a fake google map
    # A real map url might block automated requests, so we just verify it doesn't hard crash
    response = client.get("/resolve-url?url=https://www.google.com")
    assert response.status_code == 200
    data = response.json()
    assert "expanded_url" in data
