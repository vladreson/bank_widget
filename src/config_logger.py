import logging
from pathlib import Path


def setup_logger(
    name: str, log_file: str, level: int = logging.DEBUG
) -> logging.Logger:
    """Настройка логгера для модуля"""
    # Создаем папку logs если ее нет
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Очищаем существующие handlers
    if logger.handlers:
        logger.handlers.clear()

    # Настройка форматера
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Настройка file handler
    file_handler = logging.FileHandler(
        filename=logs_dir / log_file,
        mode="w",  # Перезаписываем файл при каждом запуске
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    logger.addHandler(file_handler)
    return logger
