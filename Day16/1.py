#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from enum import Enum

setrecursionlimit(10000)


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


def dfs(mirrors, coords, direction, s):
    x, y = coords
    if x < 0 or y < 0 or x >= len(mirrors[0]) or y >= len(mirrors) or (coords, direction) in s:
        return
    s.add((coords, direction))
    match mirrors[y][x], direction:
        case ('/', Direction.UP) | ('\\', Direction.DOWN):
            dfs(mirrors, (x + 1, y), Direction.RIGHT, s)
        case ('/', Direction.RIGHT) | ('\\', Direction.LEFT):
            dfs(mirrors, (x, y - 1), Direction.UP, s)
        case ('/', Direction.DOWN) | ('\\', Direction.UP):
            dfs(mirrors, (x - 1, y), Direction.LEFT, s)
        case ('/', Direction.LEFT) | ('\\', Direction.RIGHT):
            dfs(mirrors, (x, y + 1), Direction.DOWN, s)
        case ('.', d) | ('|', (Direction.UP | Direction.DOWN) as d) | ('-', (Direction.RIGHT | Direction.LEFT) as d):
            dfs(mirrors, (x + d.value[0], y + d.value[1]), d, s)
        case ('|', _):
            dfs(mirrors, (x, y - 1), Direction.UP, s)
            dfs(mirrors, (x, y + 1), Direction.DOWN, s)
        case ('-', _):
            dfs(mirrors, (x + 1, y), Direction.RIGHT, s)
            dfs(mirrors, (x - 1, y), Direction.LEFT, s)


mirrors = [line.strip() for line in stdin]
s = set()
dfs(mirrors, (0, 0), Direction.RIGHT, s)
print(len({coords for coords, _ in s}))