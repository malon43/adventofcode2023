#!/usr/bin/env python3

from sys import stdin

DIRECTIONS = {'3': (0, -1), '1': (0, 1), '2': (-1, 0), '0': (1, 0)}
ORDER = '01230'

inp = [(x[7], int(x[2:7], base=16)) for _, _, x in map(str.split, map(str.strip, stdin))]
nodes = [(0, 0)]
posx = 0
posy = 0
for i, (d, n) in enumerate(inp):
    dx, dy = DIRECTIONS[d]
    offset = (d + inp[(i + 1) % len(inp)][0] in ORDER) - (d + inp[(i - 1) % len(inp)][0] in ORDER)
    posx += dx * (n + offset)
    posy += dy * (n + offset)
    nodes.append((posx, posy))

print(sum(nodes[i][0] * (nodes[i + 1][1] - nodes[i - 1][1]) for i in range(1, len(nodes) - 1)) // 2)

