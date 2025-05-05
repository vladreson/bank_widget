import os
from decimal import Decimal
from typing import Any
from typing import Dict
from typing import Union

import requests


def convert_to_rub(
    transaction: Dict[str, Union[str, float, Decimal]],
) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с обязательными ключами:
                    - 'amount': Union[float, Decimal]
                    - 'currency': str

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: При ошибках API или неподдерживаемой валюте
    """
    # Явная проверка и приведение типов
    try:
        amount = transaction["amount"]
        currency = transaction["currency"]

        # Преобразование amount в float
        amount_float = (
            float(amount) if not isinstance(amount, float) else amount
        )

        # Проверка типа currency
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string")

    except KeyError as e:
        raise ValueError(f"Отсутствует обязательное поле: {e}")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Некорректный тип данных: {e}")

    if currency == "RUB":
        return amount_float

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Неподдерживаемая валюта: {currency}")

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        rates_data: Dict[str, Any] = response.json()
        rate = float(rates_data["rates"]["RUB"])

        return round(amount_float * rate, 2)

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка API: {str(e)}")
    except (KeyError, ValueError) as e:
        raise ValueError(f"Ошибка обработки данных: {str(e)}")
