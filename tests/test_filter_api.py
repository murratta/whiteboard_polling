from fastapi.testclient import TestClient
from backend.app import app
from config import ROOM_ID

client = TestClient(app)

def test_filter_api():
    payload = {
        "image_data": [1, 2, 3],
        "width": 1,
        "height": 1,
        "filter_name": "blur"
    }
    res = client.post(f"/filter/{ROOM_ID}", json=payload)
    assert res.status_code == 200
    assert res.json()["image_data"] == payload["image_data"]
