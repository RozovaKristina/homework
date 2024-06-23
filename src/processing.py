from typing import List, Dict, Any


def filter_by_state(inform_state: list[dict[str, Any]], state_ad="EXECUTED") -> list[dict[str, Any]]:
 """Функция фильтрации операций по ключу state"""
    
    list_state: list[dict[str]] = []
 
    for key in inform_state:
      if key.get("state") == state_ad:
        list_state.append(key)
    return list_state
def sort_by_date():

