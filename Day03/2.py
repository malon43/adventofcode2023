#!/usr/bin/env python3

from sys import stdin
from re import finditer

engine = [line.strip() for line in stdin]


def assign_gear_numbers(grs, x, y, number):
    if engine[y][x] != '*':
        return
    grs.setdefault((x, y), []).append(number)


gears = {}

for y, line in enumerate(engine):
    for n in finditer('[0-9]+', line):
        xstart = n.start()
        xend = n.end()
        number = int(n.group(0))

        if xstart > 0:
            for d in (-1, 0, 1):
                if len(engine) > y + d >= 0:
                    assign_gear_numbers(gears, xstart - 1, y + d, number)

        for d in (-1, 1):
            if len(engine) > y + d >= 0:
                for x in range(xstart, xend):
                    assign_gear_numbers(gears, x, y + d, number)

        if len(engine[0]) > xend:
            for d in (-1, 0, 1):
                if len(engine) > y + d >= 0:
                    assign_gear_numbers(gears, xend, y + d, number)

print(sum(g[0] * g[1] for g in gears.values() if len(g) == 2))

