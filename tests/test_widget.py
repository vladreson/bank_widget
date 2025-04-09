import unittest

from src.widget import get_date
from src.widget import mask_account_card


class TestWidgetFunctions(unittest.TestCase):
    def test_mask_account_card(self):
        self.assertEqual(
            mask_account_card("Visa Platinum 7000792289606361"),
            "Visa Platinum 7000 79** **** 6361")
        self.assertEqual(
            mask_account_card("Счет 73654108430135874305"),
            "Счет **4305")

    def test_get_date(self):
        self.assertEqual(get_date("2018-07-11T02:26:18.671407"), "11.07.2018")


if __name__ == "__main__":
    unittest.main()
