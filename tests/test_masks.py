from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest


@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "70007 92** **** 6361"),
    (" ", None)
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("73654108430135874315", "**4315"),
    (" ", None)
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected

