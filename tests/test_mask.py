import pytest
from src.masks import mask_card_number, mask_account_number

@pytest.fixture
def card_numbers():
    return ["1234567890123456", "4111111111111111", "5555555555554444"]

@pytest.fixture
def account_numbers():
    return ["1234567890", "9876543210123456", "1111111111111111"]

@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("4111111111111111", "4111 11** **** 1111")
])
def test_get_mask_card_number(card_number, expected):
    assert mask_card_number(card_number) == expected

def test_get_mask_account(account_numbers):
    for acc in account_numbers:
        assert mask_account_number(acc) == "**" + acc[-4:]