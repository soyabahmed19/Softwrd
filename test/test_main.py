from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_allocate_vehicle():
    response = client.post("/allocate", json={"employee_id": 1, "vehicle_id": 1, "date": "2024-10-25"})
    assert response.status_code == 200
    assert response.json() == {"message": "Vehicle allocated successfully."}

def test_get_allocation_history():
    response = client.get("/allocations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  
