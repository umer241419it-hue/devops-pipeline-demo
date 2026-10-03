import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page_status_code(client):
    """Test that '/' route returns HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200

def test_home_page_content(client):
    """Test that '/' route contains expected text."""
    response = client.get("/")
    data = response.get_data(as_text=True)
    assert "DevOps Pipeline Demo" in data
    assert "Application deployed successfully through the DevOps pipeline." in data

def test_health_status_code(client):
    """Test that '/health' route returns HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200

def test_health_response_payload(client):
    """Test that '/health' route returns expected healthy JSON response."""
    response = client.get("/health")
    json_data = response.get_json()
    assert json_data is not None
    assert json_data.get("status") == "healthy"
    assert json_data.get("service") == "devops-pipeline-demo"
