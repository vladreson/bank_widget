import re
from collections import Counter
from typing import Dict
from typing import List
from typing import Union

Transaction = Dict[str, Union[str, float]]


def filter_by_description(transactions: List[Transaction], keyword: str) -> List[Transaction]:
    keyword = str(keyword)  # Приводим keyword к строке
    return [tx for tx in transactions if re.search(keyword, str(tx.get('description', '')), re.IGNORECASE)]


def count_transaction_categories(transactions: List[Transaction]) -> Dict[str, int]:
    counter: Counter = Counter()  # Типизация переменной counter
    for tx in transactions:
        description = str(tx.get('description', ''))
        counter[description] += 1
    return dict(counter)
