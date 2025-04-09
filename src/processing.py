def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует операции по статусу."""
    return [op for op in operations if op.get("state") == state]

def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате."""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)