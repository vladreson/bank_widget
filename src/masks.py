from src.config_logger import setup_logger

# Инициализация логгера
logger = setup_logger("masks", "masks.log")


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета (последние 4 цифры)"""
    try:
        if len(account_number) < 4:
            logger.error(f"Account number too short: {account_number}")
            return account_number

        masked = "**" + account_number[-4:]
        logger.info(f"Account number masked: {account_number} -> {masked}")
        return masked
    except Exception as e:
        logger.exception(f"Error masking account number: {str(e)}")
        return account_number


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты (формат XXXX XX** **** XXXX)"""
    try:
        card_number = card_number.replace(" ", "")
        if len(card_number) != 16:
            logger.error(f"Invalid card number length: {card_number}")
            return card_number

        masked = (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        )
        logger.info(f"Card number masked: {card_number} -> {masked}")
        return masked
    except Exception as e:
        logger.exception(f"Error masking card number: {str(e)}")
        return card_number
