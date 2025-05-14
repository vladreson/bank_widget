from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.utils.file_reader import read_json_file


@pytest.fixture
def sample_json_data():
    return '[{"id": 1, "amount": 100}]'


def test_read_valid_json(tmp_path, sample_json_data):
    file = tmp_path / "test.json"
    file.write_text(sample_json_data)
    assert read_json_file(file) == [{"id": 1, "amount": 100}]


@patch("builtins.open", mock_open(read_data="invalid json"))
def test_read_invalid_json():
    assert read_json_file("bad.json") == []
