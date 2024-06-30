from typing import Any


def filter_by_state(inform_state: list[dict[str, str | int]], state_ad="EXECUTED") -> list[dict[str, str | int]]:
    """Функция фильтрации операций по ключу state"""

    list_state = []

    for key in inform_state:
        if key.get("state") == state_ad:
            list_state.append(key)
    return list_state


def sort_by_date(original_list: list[dict[str, Any], None], reverse_list: bool = True) -> list[dict[str, Any], None]:
    """Функция сортировки операций по дате"""

    sorted_list = sorted(original_list, key=lambda date: date.get("date"), reverse=reverse_list)
    return sorted_list
