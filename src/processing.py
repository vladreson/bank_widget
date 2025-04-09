def filter_by_state(operations, state='EXECUTED'):
    """
    Фильтрует список операций по значению ключа 'state'.

    :param operations: Список словарей с операциями.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [operation for operation in operations if operation.get(
        'state') == state]


def sort_by_date(operations, reverse=True):
    """
    Сортирует список операций по дате.

    :param operations: Список словарей с операциями.
    :param reverse: Если True, сортировка по убыванию (по умолчанию True).
    :return: Отсортированный список словарей.
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse)
