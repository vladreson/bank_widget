import pandas as pd
from unittest.mock import patch, mock_open
import pytest
from src.main import (
    read_transactions_json,
    read_transactions_csv,
    read_transactions_excel,
    filter_by_description,
    prompt_status
)


@pytest.fixture
def mock_json_file():
    return '[{"state": "EXECUTED", "date": "2025-05-14", "amount": 100.0, "currency_code": "RUB", "description": "Payment to vendor"}]'


@pytest.fixture
def mock_csv_file():
    return '''state;date;amount;currency_code;description
EXECUTED;2025-05-14;100.0;RUB;Payment to vendor
'''


@pytest.fixture
def mock_excel_file():
    return pd.DataFrame([{
        "state": "EXECUTED",
        "date": "2025-05-14",
        "amount": 100.0,
        "currency_code": "RUB",
        "description": "Payment to vendor"
    }])


def test_read_transactions_json(mock_json_file):
    """Тест на чтение JSON-файла."""
    with patch("builtins.open", mock_open(read_data=mock_json_file)):
        transactions = read_transactions_json()
    assert len(transactions) == 1
    assert transactions[0]["state"] == "EXECUTED"
    assert transactions[0]["amount"] == 100.0


def test_read_transactions_csv(mock_csv_file):
    """Тест на чтение CSV-файла."""
    with patch("builtins.open", mock_open(read_data=mock_csv_file)):
        transactions = read_transactions_csv('mock_file.csv')  # Читаем CSV с помощью mock_open

    # Проверяем, что данные корректно прочитаны
    assert len(transactions) == 1  # Мы ожидаем одну транзакцию
    assert "state" in transactions[0]  # Проверяем наличие поля 'state'
    assert transactions[0]["state"] == "EXECUTED"  # Проверка значения 'state'
    assert transactions[0]["amount"] == 100.0  # Проверка суммы


def test_read_transactions_excel(mock_excel_file):
    """Тест на чтение Excel-файла."""
    with patch("pandas.read_excel", return_value=mock_excel_file):
        transactions = read_transactions_excel()
    assert len(transactions) == 1
    assert transactions[0]["state"] == "EXECUTED"
    assert transactions[0]["amount"] == 100.0


def test_filter_by_description():
    """Тест на фильтрацию транзакций по ключевому слову в описании."""
    transactions = [
        {"state": "EXECUTED", "date": "2025-05-14", "amount": 100.0, "currency_code": "RUB", "description": "Payment to vendor"},
        {"state": "CANCELED", "date": "2025-05-15", "amount": 50.0, "currency_code": "USD", "description": "Refund to customer"}
    ]
    filtered = filter_by_description(transactions, "vendor")
    assert len(filtered) == 1
    assert filtered[0]["description"] == "Payment to vendor"


@pytest.mark.parametrize("status_input, expected_status", [
    ("EXECUTED", "EXECUTED"),
    ("canceled", "CANCELED"),
    ("PENDING", "PENDING")
])
@patch("builtins.input")
def test_prompt_status(mock_input, status_input, expected_status):
    """Тест на ввод статуса."""
    mock_input.side_effect = lambda prompt: status_input  # Устанавливаем поведение mock_input
    status = prompt_status()
    assert status == expected_status
