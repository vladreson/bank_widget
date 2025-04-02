def mask_card_number(number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры

    Args:
        number: строка с номером карты (16-19 цифр)

    Returns:
        Замаскированный номер в формате "XXXX XX** **** XXXX"
    """
    if len(number) < 16 or not number.isdigit():
        raise ValueError("Номер карты должен содержать минимум 16 цифр")
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account_number(number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры

    Args:
        number: строка с номером счета

    Returns:
        Замаскированный номер в формате "**XXXX"
    """
    if len(number) < 4 or not number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{number[-4:]}"