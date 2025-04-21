from typing import Dict, List, Iterator, Iterable


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по коду валюты.

    Args:
        transactions: Список транзакций
        currency_code: Код валюты (например, "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {})
        if curr.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список транзакций

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер
        end: Конечный номер (включительно)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]