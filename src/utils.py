import json
from typing import List, Dict, Any
from pathlib import Path
from src.config_logger import setup_logger

# Инициализация логгера
logger = setup_logger('utils', 'utils.log')


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.
    Логирует успешные и ошибочные случаи.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not isinstance(data, list):
                logger.error(f"File {file_path} does not contain a list")
                return []

            logger.info(f"Successfully read {len(data)} items from {file_path}")
            return data

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.exception(f"Unexpected error in read_json_file: {str(e)}")
        return []