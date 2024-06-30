from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(cards_number: str) -> str:
    """Функция общей маскировки карты и счета"""
    if len(cards_number) < 16:
        return "Некорректный ввод"
    if "Счет" in cards_number:
        return  f"Счет {get_mask_account(cards_number[5:])}"
    else:
        card = get_mask_card_number(cards_number[-16:])
        masked_payment = f"{cards_number.replace(cards_number[-16:], card)} "
        return masked_payment


def get_data(data: str) -> str:
    """Функция преобразования даты"""
    if len(data) < 10:
        return "Некорректный ввод"
    else:
        return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
