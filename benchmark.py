# coding: utf-8

from random import randint
from timeit import timeit

from example import intersect


def get_data(constuctor):
    return constuctor(randint(0, 1_000_000) for _ in range(0, 10_000_000))


if __name__ == '__main__':
    d1, d2 = get_data(list), get_data(tuple)

    print(timeit(lambda: intersect(d1, d2), number=1))
