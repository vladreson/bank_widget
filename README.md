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
## Модуль decorators

### Декоратор log
Логирует выполнение функций в файл или консоль.

```python
from src.decorators import log

@log(filename="app.log")  # Логи в файл
def calculate(a, b):
    return a + b

@log()  # Логи в консоль
def greet(name):
    return f"Hello, {name}"
```

### Тестирование
```bash
pytest tests/test_decorators.py
```