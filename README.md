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

# Банковский обработчик операций

## Функционал
- Фильтрация операций по статусу (`EXECUTED`/`CANCELED`)
- Сортировка операций по дате
- Чтение данных из JSON-файла
- Конвертация валют (USD/EUR в RUB) с использованием внешнего API
- Сокрытие чувствительных данных (API keys) с помощью .env

## Установка
1. Склонируйте репозиторий:
```bash
git clone https://github.com/vladreson/bank_widget.git
cd bank_widget