#!/usr/bin/env python3

from sys import stdin
from itertools import combinations
from bisect import bisect

MULTIPLIER = 1_000_000

universe = [line.strip() for line in stdin]
galaxyless_columns = sorted(set(range(len(universe[0]))) - {x for line in universe for x, s in enumerate(line) if s == '#'})
galaxyless_rows = [y for y, line in enumerate(universe) if '#' not in line]
galaxies = [(x + bisect(galaxyless_columns, x) * (MULTIPLIER - 1), y + bisect(galaxyless_rows, y) * (MULTIPLIER - 1)) for y, line in enumerate(universe) for x, s in enumerate(line) if s == '#']
print(sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in combinations(galaxies, 2)))
