from datetime import datetime

from src.masks import mask_account_number
from src.masks import mask_card_number


def mask_account_card(account_info: str) -> str:
    if not account_info or not isinstance(account_info, str):
        raise ValueError("Неверный формат входных данных. Ожидается строка")

    if "Счет" in account_info:
        parts = account_info.split()
        if len(parts) != 2 or not parts[1].isdigit():
            raise ValueError(
                "Неверный формат номера счета. "
                "Ожидается: 'Счет XXXX' где X - цифры"
            )
        return f"{parts[0]} {mask_account_number(parts[1])}"

    parts = account_info.rsplit(' ', 1)
    if len(parts) != 2 or not parts[1].isdigit():
        raise ValueError(
            "Неверный формат номера карты. "
            "Ожидается: 'НазваниеКарты XXXX' где X - цифры"
        )
    return f"{parts[0]} {mask_card_number(parts[1])}"


def get_date(date_str: str) -> str:
    try:
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Неверный формат даты: {date_str}") from e
