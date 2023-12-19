#!/usr/bin/env python3

from sys import stdin

DIRECTIONS = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
ORDER = 'URDLU'

inp = [(d, int(n)) for d, n, _ in map(str.split, map(str.strip, stdin))]
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

