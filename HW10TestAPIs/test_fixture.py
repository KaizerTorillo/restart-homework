from fastapi.testclient import TestClient
from main import app
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
        "name": "Things",
        "author": {"name": "John Grisham", "author_id": "HYGS-1999"},
        "year_published": "2000",
    }


@pytest.fixture
def bad_payload():
    return {
        "name": 2,  # Incorrect type
        "author": {"name": "John Grisham", "author_id": "HYGS-1999"},
        "year_published": "2000",
    }


def test_incorrect_input_put_api(client, bad_payload):
    response = client.put("/books/test/", json=bad_payload)
    assert response.status_code == 422


def test_put_api(client, good_payload):
    response = client.put("/books/test/", json=good_payload)
    assert response.status_code == 200


def test_get_api(client, good_payload):
    response = client.get("/books/test/")
    assert response.status_code == 404


# def test_put_then_get_api(client, good_payload):
#   response = client.put("/books/test/", json=good_payload)
#  assert response.status_code == 200
# response = client.get("/books/test/")
# assert response.status_code == 200


# mark.parametrize is a way to put through many test cases.
# In this case, first test cast is 1 + 2, expected is 3.
# The second test case is 5 + -1 expected 4.
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, -1, 4),
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    "payload, http_code",
    [
        (
            {
                "name": "Things",
                "author": {"name": "John Grisham", "author_id": "HYGS-1999"},
                "year_published": "2000",
            },
            200,
        ),
        (
            {
                "name": 2,  # Incorrect type
                "author": {"name": "John Grisham", "author_id": "HYGS-1999"},
                "year_published": "2000",
            },
            422,
        ),
    ],
)
def test_many_put_api(payload, http_code, client):
    assert client.put("/books/test", json=payload).status_code == http_code
