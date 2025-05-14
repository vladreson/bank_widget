import os
from typing import Dict
from typing import List
from typing import Union

import pandas as pd

Transaction = Dict[str, Union[str, float]]


def read_transactions_csv(path: str = "data/transactions.csv") -> List[Transaction]:
    df = pd.read_csv(path, delimiter=';')
    return df.to_dict(orient="records")


def read_transactions_excel(path: str = "data/transactions.xlsx") -> List[Transaction]:
    df = pd.read_excel(path)
    return df.to_dict(orient="records")


def read_transactions_json(path: str = "data/transactions.json") -> List[Transaction]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл {path} не найден. Убедитесь, что он существует.")
    df = pd.read_json(path)
    return df.to_dict(orient="records")
