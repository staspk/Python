from types import SimpleNamespace
from typing import Any, Generator


def class_attributes():
    pass

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
