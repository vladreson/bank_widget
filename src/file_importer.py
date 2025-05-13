import pandas as pd
from typing import Union


def read_transactions_csv(path: str = "data/transactions.csv") -> list[dict[str, Union[str, float]]]:
    """
    Читает CSV-файл с транзакциями и возвращает список словарей.

    :param path: Путь к CSV-файлу
    :return: Список транзакций в формате словарей
    """
    df = pd.read_csv(path)
    result = df.to_dict(orient="records")
    return [{str(k): v for k, v in record.items()} for record in result]


def read_transactions_excel(path: str = "data/transactions_excel.xlsx") -> list[dict[str, Union[str, float]]]:
    """
    Читает Excel-файл с транзакциями и возвращает список словарей.

    :param path: Путь к Excel-файлу
    :return: Список транзакций в формате словарей
    """
    df = pd.read_excel(path)
    result = df.to_dict(orient="records")
    return [{str(k): v for k, v in record.items()} for record in result]
