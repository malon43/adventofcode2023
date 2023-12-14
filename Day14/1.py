#!/usr/bin/env python3

from sys import stdin


def count_load_line(line):
    total_load = 0
    pos = 0
    for i, x in enumerate(line):
        if x == 'O':
            total_load += len(line) - pos
            pos += 1
        elif x == '#':
            pos = i + 1
    return total_load


print(sum(map(count_load_line, list(zip(*map(str.strip, stdin))))))
