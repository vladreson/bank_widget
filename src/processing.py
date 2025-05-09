from typing import Dict
from typing import List
from typing import Literal


def filter_by_state(
    operations: List[Dict[str, str]],
    state: Literal["EXECUTED", "CANCELED"] = "EXECUTED",
) -> List[Dict[str, str]]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список операций (словарей с ключом 'state')
        state: Статус для фильтрации ('EXECUTED' или 'CANCELED')

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, str]], reverse: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует операции по дате (по убыванию по умолчанию).

    Args:
        operations: Список операций (словарей с ключом 'date')
        reverse: Порядок сортировки (True - новые сначала)

    Returns:
        Отсортированный список операций
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
