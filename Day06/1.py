#!/usr/bin/env python3

from sys import stdin
from math import sqrt, ceil, floor
from itertools import islice
from operator import mul
from functools import reduce


def get_number(t, d):
    x1 = floor((t - sqrt(t ** 2 - 4 * d)) / 2)
    x2 = ceil((t + sqrt(t ** 2 - 4 * d)) / 2) - 1
    return x2 - x1


print(reduce(mul, (get_number(int(i), int(j)) for i, j in zip(islice(stdin.readline().split(), 1, None), islice(stdin.readline().split(), 1, None)))))
