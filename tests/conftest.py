# tests/conftest.py
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def operations_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": (datetime.now() - timedelta(days=1)).isoformat()},
        {"id": 2, "state": "CANCELED", "date": datetime.now().isoformat()}
    ]