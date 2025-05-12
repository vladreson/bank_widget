import os
import socket
import time
from typing import Dict
from typing import Union
from urllib.parse import urlparse

import requests


def check_api_connection(api_key: str) -> Dict[str, Union[bool, str, float]]:
    """
    Проверка подключения с корректными URL endpoints

    Args:
        api_key: API ключ от apilayer

    Returns:
        {
            "dns_resolved": bool,
            "api_reachable": bool,
            "api_response_valid": bool,
            "connection_time": float,
            "error": Optional[str]
        }
    """
    result = {
        "dns_resolved": False,
        "api_reachable": False,
        "api_response_valid": False,
        "connection_time": 0.0,
        "error": None,
    }

    # Актуальные endpoints из документации
    base_url = "https://api.apilayer.com/exchangerates_data"
    endpoints = {
        "latest": f"{base_url}/latest?base=USD",
        "convert": f"{base_url}/convert?to=RUB&from=USD&amount=1",
    }

    headers = {"apikey": api_key}

    try:
        # 1. Проверка DNS
        start_time = time.time()
        domain = urlparse(base_url).netloc
        socket.gethostbyname(domain)
        result["dns_resolved"] = True

        # 2. Проверка доступности API
        try:
            # Пробуем оба основных endpoint
            for name, url in endpoints.items():
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()

                # 3. Проверка валидности ответа
                data = response.json()
                if name == "latest" and not isinstance(
                    data.get("rates"), dict
                ):
                    raise ValueError("Invalid rates format")
                elif name == "convert" and "result" not in data:
                    raise ValueError("Missing result field")

            result["api_reachable"] = True
            result["api_response_valid"] = True
            result["connection_time"] = time.time() - start_time

        except requests.exceptions.RequestException as e:
            result["error"] = f"API request failed: {str(e)}"
        except ValueError as e:
            result["error"] = f"Invalid API response: {str(e)}"

    except socket.gaierror:
        result["error"] = "DNS resolution failed"
    except Exception as e:
        result["error"] = f"Unexpected error: {str(e)}"

    return result


def print_connection_report(api_key: str):
    """Улучшенный отчет с диагностикой"""
    print("\n🔍 Running advanced connection diagnostics...")
    print(f"🔑 API Key: {'*' * 8}{api_key[-4:]}")

    checks = check_api_connection(api_key)

    print("\n📊 Connection Test Results:")
    print(f"✅ DNS Resolved: {'Yes' if checks['dns_resolved'] else '❌ No'}")
    print(
        f"✅ API Reachable: {'Yes' if checks['api_reachable'] else '❌ No'}"
    )
    print(
        f"✅ Response Valid: {'Yes' if checks['api_response_valid'] else '❌ No'}"
    )
    print(f"⏱️ Connection Time: " f"{checks['connection_time']:.2f}s")

    if checks["error"]:
        print(f"\n❌ Error Details: {checks['error']}")
        print("\n💡 Troubleshooting Tips:")
        if "404" in str(checks["error"]):
            print(
                "- Убедитесь, что используете правильные endpoints (см. документацию)"
            )
            print("- Проверьте актуальность " "API ключа")
        elif "403" in str(checks["error"]):
            print("- Неверный или неактивный API ключ")
            print("- Проверьте лимиты запросов в кабинете apilayer")

    if all(
        [
            checks["dns_resolved"],
            checks["api_reachable"],
            checks["api_response_valid"],
        ]
    ):
        print("\n🎉 All connection tests passed successfully!")
    else:
        print("\n⚠️ Service is unavailable. See details above.")


if __name__ == "__main__":
    api_key = os.getenv("EXCHANGE_RATE_API_KEY") or input(
        "Enter your API key: "
    )
    print_connection_report(api_key)
