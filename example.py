# coding: utf-8
from typing import *

from models import Person


def get_persons(numbers: Iterable[int]) -> List[int]:
    return list(
        Person.objects.filter(
            number__in=numbers
        ).values_list('id', flat=True)
    )


def intersect(ids_from_db: List[int], l2: List[int]) -> List[int]:
    result = list()
    for i in ids_from_db:
        if i in l2:
            result.append(i)
    return result
