from src.utils import read_json_file
from src.masks import mask_account_number, mask_card_number


def test_logging():
    # Тестируем utils
    print("Testing utils...")
    read_json_file("data/operations.json")  # Успешный случай
    read_json_file("nonexistent_file.json")  # Ошибочный случай

    # Тестируем masks
    print("\nTesting masks...")
    print(mask_card_number("1234567890123456"))  # Успешный случай
    print(mask_account_number("12345678"))  # Успешный случай
    print(mask_account_number("123"))  # Ошибочный случай


if __name__ == "__main__":
    test_logging()
