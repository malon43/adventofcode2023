#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from enum import Enum
from itertools import chain

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


def get_count(mirrors, coords, direction):
    s = set()
    dfs(mirrors, coords, direction, s)
    return len({c for c, _ in s})


mirrors = [line.strip() for line in stdin]
print(max(get_count(mirrors, c, d) for c, d in chain((((x, y), d) for y in range(len(mirrors)) for x, d in zip((0, len(mirrors[0]) - 1), (Direction.RIGHT, Direction.LEFT))), (((x, y), d) for x in range(len(mirrors[0])) for y, d in zip((0, len(mirrors) - 1), (Direction.DOWN, Direction.UP))))))
