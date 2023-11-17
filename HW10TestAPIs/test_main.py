from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app

def test_basic():
    assert(True)

client = TestClient(app)

def test_put_api():
    response = client.put("name/BookA", json = {
        "name" : "BookA",
        "author" : {
            "name" : "Author1",
            "author_id" : "ATH23"
        },
        "year_published" : "2000"
        
    })
    assert response.status_code == 200



