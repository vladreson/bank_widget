def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые 6 и последние 4 цифры

    Args:
        card_number: Номер карты (16-19 цифр)

    Returns:
        Замаскированный номер карты (XXXX XX** **** XXXX)
    """
    if len(card_number) < 16:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры

    Args:
        account_number: Номер счета

    Returns:
        Замаскированный номер счета (**XXXX)
    """
    return f"**{account_number[-4:]}" if len(account_number) > 4 else account_number