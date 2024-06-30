
from src.widget import mask_account_card
from src.widget import get_data
import pytest


@pytest.mark.parametrize("value, expected", [
    ("Maestro 1596837868705199", "Maestro 15968 37** **** 5199 "),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 89909 22** **** 5229 "),
    ("Счет 73654108430135874305", "Счет **4305"),
    (" ", "Некорректный ввод")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("07-11", "Некорректный ввод"),
    (" ", "Некорректный ввод")
])
def test_get_data(value, expected):
    assert get_data(value) == expected
