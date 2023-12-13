#!/usr/bin/env python3

from sys import stdin

tables = []
while l := stdin.readline().strip():
    tables.append([l])
    while l := stdin.readline().strip():
        tables[-1].append(l)

def get_number_of_rows(table):
    yield from (i + 1 for i in range(len(table) - 1) if all(i - j < 0 or i + j + 1 >= len(table) or table[i - j] == table[i + j + 1] for j in range(len(table))))

def solve(table):
    table = [list(line) for line in table]
    a1 = next(get_number_of_rows(table), None)
    b1 = next(get_number_of_rows(list(zip(*table))), None)
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = '.' if table[i][j] == '#' else '#'
            for a2 in get_number_of_rows(table):
                if a1 != a2:
                    return a2 * 100
            for b2 in get_number_of_rows(list(zip(*table))):
                if b1 != b2:
                    return b2
            table[i][j] = '.' if table[i][j] == '#' else '#'

print(sum(map(solve, tables)))