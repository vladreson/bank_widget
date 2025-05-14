from typing import Dict
from typing import Union

from src.file_importer import read_transactions_csv
from src.file_importer import read_transactions_excel
from src.file_importer import read_transactions_json
from src.transaction_utils import filter_by_description

Transaction = Dict[str, Union[str, float]]


VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def prompt_status() -> str:
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n")
        if status.upper() in VALID_STATUSES:
            print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
            return status.upper()
        else:
            print(f"Статус операции \"{status}\" недоступен.")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = read_transactions_json()
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_csv()
    elif choice == "3":
        print("Для обработки выбран Excel-файл.")
        transactions = read_transactions_excel()
    else:
        print("Неверный выбор файла.")
        return

    status = prompt_status()
    filtered = [tx for tx in transactions if str(tx.get("state", "")).upper() == status]

    if input("Отсортировать операции по дате? Да/Нет\n").lower() == "да":
        direction = input("Отсортировать по возрастанию или по убыванию? \n").lower()
        reverse = direction == "по убыванию"
        filtered.sort(key=lambda tx: tx.get("date", ""), reverse=reverse)

    if input("Выводить только рублевые транзакции? Да/Нет\n").lower() == "да":
        filtered = [tx for tx in filtered if tx.get("currency_name", "").lower() == "рубль"]

    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower() == "да":
        keyword = input("Введите слово: ")
        filtered = filter_by_description(filtered, keyword)

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered)}\n")
    for tx in filtered:
        print(f"{tx.get('date')} {tx.get('description')}\n{tx.get('from', '')} -> {tx.get('to', '')}\nСумма: {tx.get('amount')} {tx.get('currency_code')}\n")


if __name__ == "__main__":
    main()
