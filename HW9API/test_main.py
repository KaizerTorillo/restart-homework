from fastapi.testclient import TestClient
from fastapi import FastAPI
from newmain import app


def test_basic_example():
    # pass
    assert True


client = TestClient(app)


def test_put_api():
    response = client.put(
        "items/T240",
        json={
            "name": "Product X",
            "quantity": 10,
            "serial_num": "H897",
            "origin": {"country": "Ethiopia", "production_date": "10 Aug"},
        },
    )
    assert response.status_code == 200


app = FastAPI()

# use pytest -vvl in terminal to test
