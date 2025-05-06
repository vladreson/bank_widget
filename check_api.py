import os
from dotenv import load_dotenv
from pathlib import Path
import requests


def load_env():
    """Безопасная загрузка .env"""
    env_path = Path(__file__).parent / '.env'
    try:
        load_dotenv(env_path, encoding='utf-8')
    except UnicodeDecodeError:
        print("❌ Ошибка: Некорректная кодировка .env файла")
        print("Пересохраните файл в UTF-8 (без BOM)")
        exit(1)


def check_api():
    """Проверка подключения к API"""
    load_env()

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not api_key:
        print("❌ API ключ не найден в .env")
        exit(1)

    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {"apikey": api_key}

    try:
        print("⌛ Проверяем подключение к API...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        rate = response.json()["rates"]["RUB"]
        print(f"✅ Успех! Текущий курс: 1 USD = {rate} RUB")
    except Exception as e:
        print(f"❌ Ошибка API: {e}")


if __name__ == "__main__":
    check_api()