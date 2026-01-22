from typing import Iterator


def iterate_list(items:list, step:int) -> Iterator[list]:
    if step <= 0:
        raise Exception("iterate_list(): step <= 0")

    LENGTH = len(items)
    section = []
    part = 0
    for i in range(LENGTH):
        section.append(items[i])
        part += 1
        if part == step or i == LENGTH-1:
            yield section
            section = []
            part = 0
