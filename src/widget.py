from src.masks import get_mask_card_number
from src.masks import get_mask_account

def mask_account_card(cards_number: str) -> str | None:
    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[5:])}"
        return mask_account
    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card

def get_data(data: str) -> str | None:
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
