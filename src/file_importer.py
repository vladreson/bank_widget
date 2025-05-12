from typing import Any
from typing import Dict
from typing import Hashable
from typing import List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict[Hashable, Any]]:
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_transactions_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
