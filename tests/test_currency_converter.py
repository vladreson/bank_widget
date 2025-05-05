import pytest
from unittest.mock import patch
from src.external_api.currency_converter import convert_to_rub

@pytest.fixture
def rub_transaction():
    return {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'RUB'}
        }
    }

@pytest.fixture
def usd_transaction():
    return {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }

@patch('requests.get')
def test_convert_rub(mock_get, rub_transaction):
    assert convert_to_rub(rub_transaction) == 100.0
    mock_get.assert_not_called()

@patch('requests.get')
def test_convert_usd(mock_get, usd_transaction):
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75.5}}
    mock_get.return_value.status_code = 200
    assert convert_to_rub(usd_transaction) == 755.0