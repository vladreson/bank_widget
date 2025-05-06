from typing import Dict, Union, Optional, Any
import requests
import os
from time import sleep


class ExchangeAPI:
    """Класс для работы с API обменных курсов с полной типизацией"""

    def __init__(self) -> None:
        self.timeout: int = 15
        self.max_retries: int = 2
        self.base_url: str = "https://api.apilayer.com/exchangerates_data/"
        self.headers: Dict[str, str] = {
            "apikey": os.getenv("EXCHANGE_RATE_API_KEY", "")
        }

    def _fetch_rate(self, currency: str) -> Optional[float]:
        """Основной метод получения курса с явной типизацией"""
        params: Dict[str, str] = {"base": currency, "symbols": "RUB"}

        try:
            response: requests.Response = requests.get(
                f"{self.base_url}latest",
                headers=self.headers,
                params=params,
                timeout=self.timeout,
            )
            response.raise_for_status()
            response_data: Dict[str, Any] = response.json()
            return float(response_data["rates"]["RUB"])
        except (requests.exceptions.RequestException, KeyError, ValueError):
            return None

    def get_exchange_rate(self, currency: str) -> float:
        """Получает курс с повторными попытками и гарантированным возвратом float"""
        for _ in range(self.max_retries):
            rate: Optional[float] = self._fetch_rate(currency)
            if rate is not None:
                return rate
            sleep(1)
        raise ConnectionError(f"Не удалось получить курс для {currency}")


def convert_to_rub(transaction: Dict[str, Union[str, float, int]]) -> float:
    """
    Полностью типизированная функция конвертации валюты.

    Args:
        transaction: Словарь с обязательными ключами:
                    - 'amount': Union[float, int]
                    - 'currency': str

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: При ошибках валидации или API
    """
    amount: float
    currency: str

    try:
        amount = float(transaction["amount"])
        currency = str(transaction["currency"]).upper()
    except (KeyError, ValueError, TypeError) as e:
        raise ValueError(f"Некорректные данные транзакции: {e}")

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Неподдерживаемая валюта: {currency}")

    api: ExchangeAPI = ExchangeAPI()
    try:
        rate: float = api.get_exchange_rate(currency)
        return round(amount * rate, 2)
    except ConnectionError as e:
        raise ValueError(str(e))
