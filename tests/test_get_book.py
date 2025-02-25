import uuid

from starlette.testclient import TestClient

from app.main import app


class TestGetBook:
    base_url: str
    client: TestClient

    def setup_method(self):
        self.base_url = "http://localhost:8000"
        self.client = TestClient(app)

    def test_request_should_get_200(self):
        book_id = uuid.uuid4()
        response = self.client.get(f"/books/{book_id}")
        assert response.status_code == 200
