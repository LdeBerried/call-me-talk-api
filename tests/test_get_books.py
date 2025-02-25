from starlette.testclient import TestClient

from app.main import app


class TestGetBooks:
    base_url: str
    client: TestClient

    def setup_method(self):
        self.base_url = "http://localhost:8000"
        self.client = TestClient(app)

    def test_request_should_get_200_for_v1(self):
        response = self.client.get("/v1/books")
        assert response.status_code == 200

    def test_request_should_get_404_for_v2(self):
        response = self.client.get("/v2/books")
        assert response.status_code == 404
