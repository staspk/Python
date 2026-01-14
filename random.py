import string, random
from typing import Any, Generator


class Random():
    def string(len:int, of=string.ascii_letters+string.digits) -> str:
        """
        returns a randomized string
        """
        return ''.join(random.choices(of, k=len))
    
def next_random_pop(set:set) -> Generator[Any]:
    while set.__len__() > 0:
        value = random.choice(tuple(set))
        set.remove(value)
        yield value

def random_pop(set:set) -> Any:
    if set.__len__() > 0:
        value = random.choice(tuple(set))
        set.remove(value)
        return value