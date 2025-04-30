"""Tests for user operations"""

def test_create_user(client):
    """Creates a user and verifies it's listed."""

    response1 = client.get("/users")
    assert response1.status_code == 200
    data = response1.json()
    assert isinstance(data, list)
    assert len(data) == 0

    response2 = client.post("/users/create", json={"username": "testuser"})
    assert response2.status_code == 200
    data = response2.json()
    assert data["status"] == "Ok"
    assert data["message"] == "User created successfully"
    assert data["result"]["username"] == "testuser"
    assert "id" in data["result"]

    response3 = client.get("/users")
    assert response3.status_code == 200
    data = response3.json()
    assert isinstance(data, list)
    assert len(data) == 1

def test_get_user_by_id(client):
    """Fetches a user by ID after creation."""

    create_response = client.post("/users/create", json={"username": "anotheruser"})
    user_id = create_response.json()["result"]["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == "anotheruser"

def test_delete_user(client):
    """Deletes a user and confirms it's removed."""

    # Create
    create_response = client.post("/users/create", json={"username": "user_to_delete"})
    user_id = create_response.json()["result"]["id"]

    # Delete
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

    # Delete check
    get_response = client.get(f"/{user_id}")
    assert get_response.status_code == 404
