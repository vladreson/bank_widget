import os
from datetime import datetime
from datetime import timedelta
from typing import Optional
from typing import TypedDict
from typing import Dict, Union

import requests


class ExchangeRateResponse(TypedDict):
    """Типизированный формат ответа API"""

    success: bool
    timestamp: Optional[int]
    base: str
    date: str
    rates: Dict[str, float]


class CacheEntry(TypedDict):
    """Типизированный формат записи кеша"""

    rates: Dict[str, float]
    expiry: datetime


class ExchangeRatesAPI:
    """Класс для работы с Exchange Rates Data API"""

    def __init__(self, api_key: str) -> None:
        """
        Инициализация API клиента

        Args:
            api_key: Ключ для доступа к API
        """
        self.base_url = "https://api.apilayer.com/exchangerates_data"
        self.headers = {"apikey": api_key}
        self.timeout = 15
        self.cache: Dict[str, CacheEntry] = {}
        self.cache_expiry = timedelta(hours=1)

    def _make_request(
        self, endpoint: str, params: Optional[Dict[str, str]] = None
    ) -> ExchangeRateResponse:
        """
        Выполняет запрос к API

        Args:
            endpoint: API endpoint
            params: Параметры запроса

        Returns:
            Ответ API в типизированном формате

        Raises:
            ValueError: При ошибках запроса
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(
                url, headers=self.headers, params=params, timeout=self.timeout
            )
            response.raise_for_status()
            data: ExchangeRateResponse = response.json()
            return data
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid API response: {str(e)}")

    def get_rates(self, base_currency: str = "USD") -> Dict[str, float]:
        """
        Получает текущие курсы валют

        Args:
            base_currency: Базовая валюта

        Returns:
            Словарь с курсами валют (валюта -> курс)

        Raises:
            ValueError: При ошибках API
        """
        cache_key = f"rates_{base_currency}"

        # Проверка кеша с правильными типами
        if cache_key in self.cache:
            cached = self.cache[cache_key]
            if datetime.now() < cached["expiry"]:
                return cached["rates"]

        data = self._make_request("latest", {"base": base_currency})

        if not isinstance(data.get("rates"), dict):
            raise ValueError("Invalid rates format in API response")

        # Создаем запись кеша с правильными типами
        rates = {
            currency: float(rate) for currency, rate in data["rates"].items()
        }
        cache_entry: CacheEntry = {
            "rates": rates,
            "expiry": datetime.now() + self.cache_expiry,
        }
        self.cache[cache_key] = cache_entry

        return rates

    def convert(
        self, amount: float, from_currency: str, to_currency: str
    ) -> float:
        """
        Конвертирует сумму между валютами

        Args:
            amount: Сумма для конвертации
            from_currency: Исходная валюта
            to_currency: Целевая валюта

        Returns:
            Сконвертированная сумма (округленная до 2 знаков)

        Raises:
            ValueError: При ошибках конвертации
        """
        if from_currency == to_currency:
            return amount

        rates = self.get_rates(from_currency)

        try:
            rate = rates[to_currency]
            return round(float(amount) * rate, 2)
        except KeyError as e:
            raise ValueError(f"Unsupported currency: {str(e)}")


def convert_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Конвертирует сумму транзакции в рубли

    Args:
        transaction: {
            "amount": число,
            "currency": "USD"/"EUR"/"RUB"
        }

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: При ошибках валидации или API
    """
    try:
        amount = float(transaction["amount"])
        currency = str(transaction["currency"]).upper()
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid transaction data: {e}")

    if currency == "RUB":
        return amount

    api = ExchangeRatesAPI(os.getenv("EXCHANGE_RATE_API_KEY"))

    try:
        rate = api.get_rates(currency)["RUB"]
        return round(amount * rate, 2)
    except KeyError:
        raise ValueError(f"Unsupported currency: {currency}")
    except ValueError as e:
        raise ValueError(f"API error: {str(e)}")

