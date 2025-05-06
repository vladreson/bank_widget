import os
from dotenv import load_dotenv
from src.external_api import convert_to_rub


def test_api_connection():
    """Тест подключения к API"""
    load_dotenv()

    test_cases = [
        {"amount": 100, "currency": "USD"},
        {"amount": 50, "currency": "EUR"},
        {"amount": 1000, "currency": "RUB"}
    ]

    for case in test_cases:
        try:
            result = convert_to_rub(case)
            print(f"✅ {case['amount']} {case['currency']} = {result} RUB")
        except ValueError as e:
            print(f"❌ Ошибка для {case}: {e}")


if __name__ == "__main__":
    test_api_connection()