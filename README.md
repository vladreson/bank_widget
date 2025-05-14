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
```

# Финансовый анализ

## Новая функциональность

- Добавлена поддержка импорта финансовых транзакций из CSV и Excel файлов.
- Реализованы функции `read_transactions_csv` и `read_transactions_excel` в модуле `file_importer.py`.
- Добавлены соответствующие тесты с использованием `pytest` и `unittest.mock`.


## Новая функциональность

### Поиск операций
- Поиск по описанию с регулярными выражениями (`search_by_description()`)
- Подсчет операций по категориям (`count_categories()`)

### Основной интерфейс
Запустите `main.py` для интерактивной работы:
1. Выбор типа файла (JSON/CSV/Excel)
2. Фильтрация по статусу
3. Дополнительные фильтры (дата, валюта, описание)
4. Просмотр результатов

Пример:
```python
from src.operations import search_by_description

operations = [...]  # список операций
found = search_by_description(operations, 'перевод')


