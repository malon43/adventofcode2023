#!/usr/bin/env python3

from sys import stdin
from re import finditer


engine = [line.strip() for line in stdin]


def is_symbol(s):
    return s != '.' and not s.isdigit()


def is_part_number(xstart, xend, y):
    return (
        (xstart > 0 and any(is_symbol(engine[y + d][xstart - 1]) for d in (-1, 0, 1) if len(engine) > y + d >= 0))
        or any(is_symbol(engine[y + d][x]) for d in (-1, 1) if len(engine) > y + d >= 0 for x in range(xstart, xend))
        or (xend < len(engine[0]) and any(is_symbol(engine[y + d][xend]) for d in (-1, 0, 1) if len(engine) > y + d >= 0))
    )


print(sum(int(n.group(0)) for y, line in enumerate(engine) for n in finditer('[0-9]+', line) if is_part_number(n.start(), n.end(), y)))

