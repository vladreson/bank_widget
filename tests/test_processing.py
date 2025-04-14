import pytest
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict

def test_filter_by_state() -> None:
    """
    Тестирует фильтрацию операций по статусу EXECUTED.
    """
    operations: List[Dict[str, str]] = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02"}
    ]
    filtered = filter_by_state(operations)
    assert len(filtered) == 1
    assert filtered[0]["state"] == "EXECUTED"

def test_sort_by_date() -> None:
    """
    Тестирует сортировку операций по дате.
    """
    operations: List[Dict[str, str]] = [
        {"date": "2023-01-02"},
        {"date": "2023-01-01"}
    ]
    sorted_ops = sort_by_date(operations, reverse=False)
    assert sorted_ops[0]["date"] == "2023-01-01"