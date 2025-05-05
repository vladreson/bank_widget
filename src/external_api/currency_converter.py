import os
from typing import Dict
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict) -> Optional[float]:
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        if currency == 'RUB':
            return amount

        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()
        rate = float(response.json()['rates']['RUB'])  # Явно приводим к float
        return round(amount * rate, 2)  # round возвращает float
    except (KeyError, requests.RequestException, ValueError):
        return None
