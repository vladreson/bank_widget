import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    print("Ошибка: API ключ не найден в .env файле!")
    exit()

url = "https://api.apilayer.com/exchangerates_data/latest?base=USD"
headers = {"apikey": API_KEY}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    print("API работает корректно!")
    print("Пример курса USD -> RUB:", response.json()['rates']['RUB'])

except Exception as e:
    print("Ошибка при запросе к API:")
    print(e)