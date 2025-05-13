from unittest.mock import patch

import pandas as pd

from src.file_importer import read_transactions_csv
from src.file_importer import read_transactions_excel


# Тест для функции чтения CSV
@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    # Мокируем результат pandas.read_csv
    mock_read_csv.return_value = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "success",
                "date": "2025-01-01",
                "amount": 100.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "A",
                "to": "B",
                "description": "Test Transaction 1",
            },
            {
                "id": 2,
                "state": "failed",
                "date": "2025-01-02",
                "amount": 200.0,
                "currency_name": "EUR",
                "currency_code": "EUR",
                "from": "C",
                "to": "D",
                "description": "Test Transaction 2",
            },
        ]
    )

    # Ожидаемый результат
    expected_result = [
        {
            "id": 1,
            "state": "success",
            "date": "2025-01-01",
            "amount": 100.0,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "A",
            "to": "B",
            "description": "Test Transaction 1",
        },
        {
            "id": 2,
            "state": "failed",
            "date": "2025-01-02",
            "amount": 200.0,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "C",
            "to": "D",
            "description": "Test Transaction 2",
        },
    ]

    # Вызов функции
    result = read_transactions_csv("dummy_path.csv")

    # Проверка
    assert result == expected_result


# Тест для функции чтения Excel
@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel):
    # Мокируем результат pandas.read_excel
    mock_read_excel.return_value = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "success",
                "date": "2025-01-01",
                "amount": 150.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "A",
                "to": "B",
                "description": "Test Excel Transaction 1",
            },
            {
                "id": 2,
                "state": "failed",
                "date": "2025-01-02",
                "amount": 250.0,
                "currency_name": "EUR",
                "currency_code": "EUR",
                "from": "C",
                "to": "D",
                "description": "Test Excel Transaction 2",
            },
        ]
    )

    # Ожидаемый результат
    expected_result = [
        {
            "id": 1,
            "state": "success",
            "date": "2025-01-01",
            "amount": 150.0,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "A",
            "to": "B",
            "description": "Test Excel Transaction 1",
        },
        {
            "id": 2,
            "state": "failed",
            "date": "2025-01-02",
            "amount": 250.0,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "C",
            "to": "D",
            "description": "Test Excel Transaction 2",
        },
    ]

    # Вызов функции
    result = read_transactions_excel("dummy_path.xlsx")

    # Проверка
    assert result == expected_result
