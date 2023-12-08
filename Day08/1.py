#!/usr/bin/env python3

from sys import stdin
from re import match
from functools import partial


directions = stdin.readline().strip()
stdin.readline()
nodes = {m.group(1): (m.group(2), m.group(3)) for m in map(partial(match, r'([^ ]+) = \(([^,]+), ([^)]+)\)'), stdin)}

node = 'AAA'
i = 0
while node != 'ZZZ':
    node = nodes[node][directions[i % len(directions)] == 'R']
    i += 1

print(i)