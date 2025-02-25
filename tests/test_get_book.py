import uuid

from starlette.testclient import TestClient

from app.main import app


class TestGetBook:
    base_url: str
    client: TestClient

    def setup_method(self):
        self.base_url = "http://localhost:8000"
        self.client = TestClient(app)

    def test_request_should_get_200_for_v1(self):
        book_id = uuid.uuid4()
        response = self.client.get(f"/v1/books/{book_id}")
        assert response.status_code == 200

    def test_request_should_get_200_for_v2(self):
        book_title = "Pride and Prejudice"
        response = self.client.get(f"/v2/books/{book_title}")
        assert response.status_code == 200
