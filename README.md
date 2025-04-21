# Банковский обработчик операций

## Функционал
- Фильтрация операций по статусу (`EXECUTED`/`CANCELED`)
- Сортировка операций по дате

## Установка
```bash
git clone https://github.com/vladreson/bank_widget.git
cd bank_widget
poetry install
```

## Пример использования
```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-02"}
]

# Фильтрация
executed_ops = filter_by_state(operations)

# Сортировка
sorted_ops = sort_by_date(operations, reverse=False)
```

## Тестирование
```bash
poetry run pytest tests/
```

## Модуль generators

### Функции:
1. `filter_by_currency(transactions, currency_code)`  
   Фильтрует транзакции по валюте. Возвращает итератор.

   Пример:
   ```python
   usd_transactions = filter_by_currency(transactions, "USD")
   print(next(usd_transactions))
   ```

2. `transaction_descriptions(transactions)`  
   Генерирует описания транзакций.

3. `card_number_generator(start, end)`  
   Генерирует номера карт в заданном диапазоне.

### Тестирование
```bash
pytest tests/test_generators.py
```