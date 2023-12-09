#!/usr/bin/env python3

from sys import stdin
from itertools import pairwise


def sequence_value_derivator(sequence):
    if (all(v == 0 for v in sequence)):
        return 0
    return sequence[0] - sequence_value_derivator([b - a for a, b in pairwise(sequence)])


print(sum(map(sequence_value_derivator, ([int(v) for v in line.split()] for line in stdin))))
