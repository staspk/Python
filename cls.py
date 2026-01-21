from typing import Any, Iterator


def class_attributes(cls) -> Iterator[Any]:
    for key,value in cls.__dict__.items():
        if key.startswith('__'): continue
        if callable(value): continue
        if isinstance(value, (classmethod, property)): continue
        yield key,value

def set_frozen_attr(instance, attr_name:str, value):
    """ bypasses: `@dataclass(frozen=True)` """
    object.__setattr__(instance, attr_name, value)