#!/usr/bin/env python3

from sys import stdin
from enum import Enum
from math import ceil


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


pipes = [line.strip() for line in stdin]


def get_next_coords(pipes, incoming_direction_from, current_coords):
    x, y = current_coords
    pipe = pipes[y][x]
    match incoming_direction_from, pipe:
        case (Direction.NORTH, '|') | (Direction.WEST, '7') | (Direction.EAST, 'F') if y + 1 < len(pipes):
            return Direction.NORTH, (x, y + 1)
        case (Direction.SOUTH, '|') | (Direction.WEST, 'J') | (Direction.EAST, 'L') if y - 1 >= 0:
            return Direction.SOUTH, (x, y - 1)
        case (Direction.WEST, '-') | (Direction.NORTH, 'L') | (Direction.SOUTH, 'F') if x + 1 < len(pipes[0]):
            return Direction.WEST, (x + 1, y)
        case (Direction.EAST, '-') | (Direction.NORTH, 'J') | (Direction.SOUTH, '7') if x - 1 >= 0:
            return Direction.EAST, (x - 1, y)
        case _:
            return None


def find_loop_length(pipes, *res):
    i = 0
    while (res := get_next_coords(pipes, *res)) is not None and pipes[res[1][1]][res[1][0]] != 'S':
        i += 1

    return res and i + 1


def get_s_pos(pipes):
    for y, line in enumerate(pipes):
        for x, p in enumerate(line):
            if p == 'S':
                return x, y


s_pos = get_s_pos(pipes)
starting_directions = [
    (Direction.NORTH, (0, 1)),
    (Direction.EAST, (1, 0)),
    (Direction.SOUTH, (0, -1)),
    (Direction.WEST, (-1, 0))
]

print(ceil(next(filter(bool, (find_loop_length(pipes, d, (s_pos[0] + dx, s_pos[1] + dy)) for d, (dx, dy) in starting_directions))) / 2))