#!/usr/bin/env python3

from sys import stdin
from math import sqrt, ceil, floor


def get_number(t, d):
    x1 = floor((t - sqrt(t ** 2 - 4 * d)) / 2)
    x2 = ceil((t + sqrt(t ** 2 - 4 * d)) / 2) - 1
    return x2 - x1


print(get_number(int(stdin.readline().split(maxsplit=1)[1].replace(' ', '')), int(stdin.readline().split(maxsplit=1)[1].replace(' ', ''))))
