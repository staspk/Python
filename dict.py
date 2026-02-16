from typing import Any


def increment_value(dict:dict, key:Any):
    if key in dict: dict[key] += 1
    else:           dict[key]  = 1

class Dict:
    def print_items(dict:dict):
        for key,value in dict.items():
            print(f'{key}: {value}')