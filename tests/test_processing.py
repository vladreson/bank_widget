from src.processing import filter_by_state, sort_by_date

# Тестовые данные
operations = [
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
    },
]

# Тестирование функции filter_by_state


def test_filter_by_state():
    filtered_operations = filter_by_state(operations, "EXECUTED")
    assert (
        len(filtered_operations) == 2
    ), "Фильтр по 'EXECUTED' работает некорректно"
    assert all(
        op["state"] == "EXECUTED" for op in filtered_operations
    ), "Не все операции имеют статус 'EXECUTED'"


# Тестирование функции sort_by_date


def test_sort_by_date():
    sorted_operations_desc = sort_by_date(operations, reverse=True)
    assert (
        sorted_operations_desc[0]["date"] == "2019-07-03T18:35:29.512364"
    ), "Сортировка по убыванию работает некорректно"

    sorted_operations_asc = sort_by_date(operations, reverse=False)
    assert (
        sorted_operations_asc[0]["date"] == "2018-06-30T02:08:58.425572"
    ), "Сортировка по возрастанию работает некорректно"


# Запуск тестов
if __name__ == "__main__":
    test_filter_by_state()
    test_sort_by_date()
    print("Все тесты прошли успешно!")
