#!/usr/bin/env python3
"""
Works only for the magical input, which I had on AOC
(and since it would be a miracle to encounter this kind of input just randomly,
I am assuming this was also true for everyone else)

I absolutely despise this solution. :-)
"""

from sys import stdin
from re import match
from functools import partial
from math import lcm

directions = stdin.readline().strip()
stdin.readline()
nodes = {m.group(1): (m.group(2), m.group(3)) for m in map(partial(match, r'([^ ]+) = \(([^,]+), ([^)]+)\)'), stdin)}

current_nodes = [node for node in nodes if node[-1] == 'A']
cycles = []

for node in nodes:
    if node[-1] != 'A':
        continue

    cycle_start = None
    cycle_length = None
    i = 0

    while cycle_length is None:
        if node[-1] == 'Z':
            if cycle_start is None:
                cycle_start = i
                cycle_start_node = node
            elif cycle_start_node != node:
                raise ValueError("This input is not magical")
            elif cycle_start % len(directions) == i % len(directions):
                cycle_length = i - cycle_start
            else:
                raise ValueError("This input is not magical")

        node = nodes[node][directions[i % len(directions)] == 'R']
        i += 1

    if cycle_start != cycle_length:
        print(node, cycle_start, cycle_length)
        raise ValueError("This input is not magical")

    cycles.append((cycle_start, cycle_length))

print(lcm(*(c[0] for c in cycles)))