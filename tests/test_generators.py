import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    expected_descriptions = [
       "Перевод организации",
       "Перевод со счета на счет",
       "Перевод со счета на счет",
       "Перевод с карты на карту",
       "Перевод организации"
    ]

    for expected in expected_descriptions:
        assert next(descriptions) == expected


def test_filter_by_currency() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


@pytest.mark.parametrize("start, stop, expected", [(1, 1, "0000 0000 0000 0001")])
def test_card_number_generator(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected
