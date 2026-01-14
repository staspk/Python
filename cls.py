from types import SimpleNamespace
from typing import Any, Generator


def class_attributes(cls) -> Generator[Any]:
    for key,value in cls.__dict__.items():
        if key.startswith('__'): continue
        if callable(value): continue
        if isinstance(value, (classmethod, property)): continue
        yield key,value

def instance_attributes(instance, keys_to_exclude:list=[]) -> Generator[Any]:
    """
    **How to Use:**
    ```python
    for attr in instance_attributes(cls_instance, keys_to_exclude=['special_key']):
        translation:str = attr.key
        marked_chapters:set[int] = attr.value
        Print.green(f'{translation} -> {str(marked_chapters)}')
    ```
    """
    for key,value in instance.__dict__.items():
        if key in keys_to_exclude: continue
        yield SimpleNamespace(key=key, value=value)

def instance_attribute_keys(instance, keys_to_exclude:list=[]) -> Generator[Any]:
    for key in instance.__dict__.keys():
        if key in keys_to_exclude: continue
        yield key

def instance_attribute_values(instance, keys_to_exclude:list=[]) -> Generator[Any]:
    for key,value in instance.__dict__.items():
        if key in keys_to_exclude: continue
        yield value
