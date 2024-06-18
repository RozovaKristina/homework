from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_data

print(get_mask_card_number("7000792289606361"))

print(get_mask_account("73654108430135874315"))

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))

print(get_data("2018-07-11T02:26:18.671407"))

help(mask_account_card)
