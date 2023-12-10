#!/usr/bin/env python3

from sys import stdin
from enum import Enum


class DirectionFrom(Enum):
    FROM_NORTH = 0
    FROM_EAST = 1
    FROM_SOUTH = 2
    FROM_WEST = 3


class OnPipe(Enum):
    NO = 0
    FROM_NORTH = 1
    FROM_SOUTH = 2


def get_next_coords(pipes, incoming_direction_from, current_coords):
    x, y = current_coords
    pipe = pipes[y][x]
    match incoming_direction_from, pipe:
        case (DirectionFrom.FROM_NORTH, '|') | (DirectionFrom.FROM_WEST, '7') | (DirectionFrom.FROM_EAST, 'F') if y + 1 < len(pipes):
            return DirectionFrom.FROM_NORTH, (x, y + 1)
        case (DirectionFrom.FROM_SOUTH, '|') | (DirectionFrom.FROM_WEST, 'J') | (DirectionFrom.FROM_EAST, 'L') if y - 1 >= 0:
            return DirectionFrom.FROM_SOUTH, (x, y - 1)
        case (DirectionFrom.FROM_WEST, '-') | (DirectionFrom.FROM_NORTH, 'L') | (DirectionFrom.FROM_SOUTH, 'F') if x + 1 < len(pipes[0]):
            return DirectionFrom.FROM_WEST, (x + 1, y)
        case (DirectionFrom.FROM_EAST, '-') | (DirectionFrom.FROM_NORTH, 'J') | (DirectionFrom.FROM_SOUTH, '7') if x - 1 >= 0:
            return DirectionFrom.FROM_EAST, (x - 1, y)
        case _:
            return None


def count_in_line(loop_set, y, line):
    count = 0
    in_loop = False
    on_pipe = OnPipe.NO
    for x, pipe in enumerate(line):
        if (x, y) not in loop_set:
            count += in_loop
            continue

        match on_pipe, pipe:
            case (OnPipe.NO, '|'):
                in_loop = not in_loop
            case (OnPipe.NO, 'L'):
                on_pipe = OnPipe.FROM_NORTH
            case (OnPipe.NO, 'F'):
                on_pipe = OnPipe.FROM_SOUTH
            case (OnPipe.FROM_NORTH, 'J') | (OnPipe.FROM_SOUTH, '7'):
                on_pipe = OnPipe.NO
            case (OnPipe.FROM_NORTH, '7') | (OnPipe.FROM_SOUTH, 'J'):
                on_pipe = OnPipe.NO
                in_loop = not in_loop
            case (OnPipe.FROM_NORTH | OnPipe.FROM_SOUTH, '-'):
                pass
            case s:
                raise RuntimeError(f'Invalid state {repr(s)} ({x}, {y})')
    return count


def count_inside_loop(pipes, *res):
    first_dir = res[0]
    loop_set = {res[1]}

    while (res := get_next_coords(pipes, *res)) is not None and pipes[res[1][1]][res[1][0]] != 'S':
        loop_set.add(res[1])

    if res is None:
        return None

    loop_set.add(res[1])

    match first_dir, res[0]:
        case (DirectionFrom.FROM_NORTH, DirectionFrom.FROM_NORTH) | (DirectionFrom.FROM_SOUTH, DirectionFrom.FROM_SOUTH):
            s_repl = '|'
        case (DirectionFrom.FROM_EAST, DirectionFrom.FROM_EAST) | (DirectionFrom.FROM_WEST, DirectionFrom.FROM_WEST):
            s_repl = '-'
        case (DirectionFrom.FROM_SOUTH, DirectionFrom.FROM_EAST) | (DirectionFrom.FROM_WEST, DirectionFrom.FROM_NORTH):
            s_repl = 'L'
        case (DirectionFrom.FROM_EAST, DirectionFrom.FROM_NORTH) | (DirectionFrom.FROM_SOUTH, DirectionFrom.FROM_WEST):
            s_repl = 'J'
        case (DirectionFrom.FROM_NORTH, DirectionFrom.FROM_WEST) | (DirectionFrom.FROM_EAST, DirectionFrom.FROM_SOUTH):
            s_repl = '7'
        case (DirectionFrom.FROM_NORTH, DirectionFrom.FROM_EAST) | (DirectionFrom.FROM_WEST, DirectionFrom.FROM_SOUTH):
            s_repl = 'F'
        case _:
            raise("Invalid configuration")
    pipes[res[1][1]] = pipes[res[1][1]].replace('S', s_repl)

    return sum(count_in_line(loop_set, *line) for line in enumerate(pipes))


def get_s_pos(pipes):
    for y, line in enumerate(pipes):
        for x, p in enumerate(line):
            if p == 'S':
                return x, y


pipes = [line.strip() for line in stdin]
s_pos = get_s_pos(pipes)

START_DIRECTIONS = [
    (DirectionFrom.FROM_NORTH, (0, 1)),
    (DirectionFrom.FROM_EAST, (1, 0)),
    (DirectionFrom.FROM_SOUTH, (0, -1)),
    (DirectionFrom.FROM_WEST, (-1, 0))
]

print(next(filter(bool, (count_inside_loop(pipes, d, (s_pos[0] + dx, s_pos[1] + dy)) for d, (dx, dy) in START_DIRECTIONS))))