from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app


def test_basic():
    assert True


client = TestClient(app)


def test_put_api():
    response = client.put(
        "/books/BookA",
        json={
            "name": "BookA",
            "author": {"name": "John Grisham", "author_id": "HYGS-1999"},
            "year_published": "2000",
        },
    )
    assert response.status_code == 200


def test_get_api():
    response = client.get("/books/")
    assert response.status_code == 200


def test_delete_api():
    response = client.delete("books/")
    assert response.status_code == 405
