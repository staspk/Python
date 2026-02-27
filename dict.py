from typing import Any
from itertools import islice


def increment_value(dict:dict, key:Any):
    if key in dict: dict[key] += 1
    else:           dict[key]  = 1

class Dict:
    def print_items(dict:dict):
        for key,value in dict.items():
            print(f'{key}: {value}')

    def key(dict:dict, index:int):
        """
        Pull key from dict by index without building a list.
        O(n) traversal, use only when dicts are very long, many operations 
        """
        return next(islice(dict.keys(), index, index+1))

    def value(dict:dict, index:int):
        """
        Pull value from dict by index without building a list.
        O(n) traversal, use only when dicts are very long, many operations
        """
        return next(islice(dict.values(), index, index+1))
