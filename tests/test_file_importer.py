from unittest.mock import patch

import pandas as pd

from src.file_importer import read_transactions_csv
from src.file_importer import read_transactions_excel


@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame(
        [
            {"date": "2025-01-01", "amount": 100.0, "currency": "USD"},
            {"date": "2025-01-02", "amount": 200.0, "currency": "EUR"},
        ]
    )

    result = read_transactions_csv("fake_path.csv")
    assert len(result) == 2
    assert result[0]["currency"] == "USD"


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame(
        [
            {"date": "2025-01-01", "amount": 150.0, "currency": "USD"},
            {"date": "2025-01-02", "amount": 250.0, "currency": "EUR"},
        ]
    )

    result = read_transactions_excel("fake_path.xlsx")
    assert len(result) == 2
    assert result[1]["amount"] == 250.0
