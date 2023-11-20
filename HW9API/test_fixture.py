from fastapi.testclient import TestClient
from newmain import app
import pytest


@pytest.fixture
def client():
    yield TestClient(
        app
    )  # Creates a test object everytime a fixture is called and removes is after.


# 1) fixture = precondition to test case. Pre-initialization of an object and return it.
# 2) Providing a matrix of inputs and receiving a matrix of outputs.
# 3) Mock - blackbox testing (not recommended, Nick thinks its bad practice)


@pytest.fixture
def good_payload():
    return {
        "name": "desk",
        "quantity": 2,
        "serial_num": "123sd",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": 2,
        "quantity": 2,
        "serial_num": "123sd",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


def test_incorrect_input_put_api(client, bad_payload):
    response = client.put("/items/test/", json=bad_payload)
    assert response.status_code == 422


def test_correct_input_api(client, good_payload):
    response = client.put("items/test/", json=good_payload)
    assert response.status_code == 200


def test_get_api(client, good_payload):
    response = client.get("/items/")
    assert response.status_code == 200


def test_put_then_get_api(client, good_payload):
    response = client.put("/items/123sd/", json=good_payload)
    assert response.status_code == 200
    response = client.get("/items/123sd/")
    assert response.status_code == 200 and response.json() == good_payload


def test_delete_api(client, good_payload):
    response = client.delete("items/123sd/")
    assert response.status_code == 200


def test_check_delete_api(client, good_payload):
    response = client.delete("items/123sd/")
    assert response.status_code == 404
