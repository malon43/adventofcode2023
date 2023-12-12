#!/usr/bin/env python3

from sys import stdin
from itertools import starmap
from functools import cache

MULTIPLIER = 5


def can_be_placed(springs, i, number):
    return i + number <= len(springs) and all(springs[k] in ('?', '#') for k in range(i, i + number)) and (i + number == len(springs) or springs[i + number] in ('.', '?'))


@cache
def backtrack(springs, numbers, i=0, j=0):
    if j >= len(numbers):
        return '#' not in springs[i:]

    if len(springs) - i < sum(numbers[j:]) + len(numbers) - j - 1:  # Optimization
        return 0

    while i < len(springs) and springs[i] == '.':
        i += 1

    if i >= len(springs):
        return 0

    if springs[i] == '#':
        return backtrack(springs, numbers, i + numbers[j] + 1, j + 1) if can_be_placed(springs, i, numbers[j]) else 0

    res = backtrack(springs, numbers, i + 1, j)
    if can_be_placed(springs, i, numbers[j]):
        res += backtrack(springs, numbers, i + numbers[j] + 1, j + 1)
    return res


print(sum(starmap(backtrack, (('?'.join((springs,) * MULTIPLIER), tuple([int(i) for i in numbers.split(',')]) * MULTIPLIER) for springs, numbers in map(str.split, map(str.strip, stdin))))))