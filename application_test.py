import pytest
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.testclient import TestClient
import time

from main import app


client = TestClient(app)


class TestCase:
    MAX_RESPONSE_TIME = 0.5

    @pytest.mark.parametrize("endpoint", ["/", "/result", "/api/classify_number?number=45", "/api/classify_number?number=4.5"])
    def test_response_time(self, endpoint):
        start_time = time.time()
        response = client.get(endpoint)
        end_time = time.time()

        response_time = end_time - start_time
        if response.status_code != 200:
            assert JSONResponse(status_code=400, content={"number":"alphabet", "error":True})

        assert response_time < TestCase.MAX_RESPONSE_TIME, f"Response too slow: {response_time:.3f}s"


