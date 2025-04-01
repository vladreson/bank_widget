from typing import Tuple
from datetime import datetime


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер счета или карты в переданной строке.

    Args:
        account_info: Строка с информацией о счете/карте (например, "Visa Platinum 7000792289606361")

    Returns:
        Строка с замаскированным номером счета/карты
    """
    parts = account_info.split()
    if parts[0] == "Счет":
        return f"Счет **{parts[-1][-4:]}"
    else:
        masked_number = f"{parts[-1][:4]} {parts[-1][4:6]}** **** {parts[-1][-4:]}"
        return " ".join(parts[:-1] + [masked_number])


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формат DD.MM.YYYY.

    Args:
        date_str: Строка с датой (например, "2018-07-11T02:26:18.671407")

    Returns:
        Дата в формате DD.MM.YYYY (например, "11.07.2018")
    """
    date_obj = datetime.strptime(date_str.split('T')[0], "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")