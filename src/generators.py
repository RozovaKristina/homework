from typing import Generator
def filter_by_currency(operations: list, currency: str) -> Generator:
    """Функция возвращает итератор из списка словарей"""
    for operation in operations:
        if operation["operationAmount"]['currency']["code"] == currency:
            yield operation



def transaction_descriptions(transactions):
    """Функция возвращает описание операций из списка словарей"""

    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Генератор номера карт"""

    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formatted_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formatted_number
