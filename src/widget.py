from datetime import datetime
from .masks import mask_account_number, mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета, используя функции из модуля masks.py

    Args:
        account_info: строка формата "Visa Platinum 7000792289606361"
                     или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером карты/счета

    Raises:
        ValueError: если входные данные не соответствуют ожидаемому формату
    """
    if not account_info or not isinstance(account_info, str):
        raise ValueError("Неверный формат входных данных. Ожидается строка.")

    if "Счет" in account_info:
        parts = account_info.split()
        if len(parts) != 2 or not parts[1].isdigit():
            raise ValueError("Неверный формат номера счета. Ожидается: 'Счет XXXX' где X - цифры")
        return f"{parts[0]} {mask_account_number(parts[1])}"

    else:  # Обработка карт
        parts = account_info.rsplit(' ', 1)
        if len(parts) != 2 or not parts[1].isdigit():
            raise ValueError("Неверный формат номера карты. Ожидается: 'НазваниеКарты XXXX' где X - цифры")
        return f"{parts[0]} {mask_card_number(parts[1])}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате ISO в формат DD.MM.YYYY
    """
    try:
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Неверный формат даты: {date_str}") from e