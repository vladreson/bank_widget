import unittest
from datetime import datetime
from src.widget import mask_account_card, get_date


class TestWidgetFunctions(unittest.TestCase):
    """Тесты для функций модуля widget"""

    def test_mask_account_card(self):
        """Тестирование маскировки карт и счетов"""
        self.assertEqual(
            mask_account_card("Visa Platinum 7000792289606361"),
            "Visa Platinum 7000 79** **** 6361"
        )
        self.assertEqual(
            mask_account_card("Счет 73654108430135874305"),
            "Счет **4305"
        )

    def test_get_date_valid_formats(self):
        """Тестирование корректного форматирования даты"""
        test_cases = [
            ("2018-07-11T02:26:18.671407", "11.07.2018"),
            ("2023-12-31T23:59:59.999999", "31.12.2023"),
            ("2020-01-01T00:00:00Z", "01.01.2020"),  # С Z в конце
            ("1999-12-31T00:00:00+00:00", "31.12.1999")  # С часовым поясом
        ]

        for input_date, expected in test_cases:
            with self.subTest(input_date=input_date):
                self.assertEqual(get_date(input_date), expected)

    def test_get_date_invalid_formats(self):
        """Тестирование обработки некорректных дат"""
        invalid_dates = [
            "не-дата",
            "2023/12/31",
            "",
            None,
            12345,
            "11.07.2018"  # Уже в неправильном формате
        ]

        for invalid_date in invalid_dates:
            with self.subTest(invalid_date=invalid_date), \
                    self.assertRaises(ValueError):
                get_date(invalid_date)


if __name__ == "__main__":
    unittest.main()