#!/usr/bin/env python3

from sys import stdin

CYCLES = 1_000_000_000


def shift_rocks(rocks):
    top_positions = [0] * len(rocks[0])
    for y, line in enumerate(rocks):
        for x, rock in enumerate(line):
            if rock == '#':
                top_positions[x] = y + 1
            elif rock == 'O':
                rocks[y][x] = '.'
                rocks[top_positions[x]][x] = 'O'
                top_positions[x] += 1
    return rocks


def cycle(rocks):
    for _ in range(4):
        rocks = list(map(list, map(reversed, zip(*shift_rocks(rocks)))))
    return rocks


def solve(rocks):
    d = {}
    for i in range(CYCLES):
        rocks = cycle(rocks)
        trocks = tuple(map(tuple, rocks))
        if trocks in d:
            break
        d[trocks] = i

    res_rocks = {v: k for k, v in d.items()}[d[trocks] + (CYCLES - i) % (i - d[trocks]) - 1]
    total_load = 0
    for n, line in enumerate(reversed(res_rocks)):
        total_load += line.count('O') * (n + 1)
    return total_load


print(solve(list(map(list, map(str.strip, stdin)))))