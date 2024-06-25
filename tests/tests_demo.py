from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_data
from src.processing import filter_by_state
from src.processing import sort_by_date
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


def test_filter_by_state(state):
    var = filter_by_state(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    ) == state


def test_sort_by_date(sort_date):
    var = sort_by_date(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    ) == sort_date
