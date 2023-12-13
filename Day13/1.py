#!/usr/bin/env python3

from sys import stdin

tables = []
while l := stdin.readline().strip():
    tables.append([l])
    while l := stdin.readline().strip():
        tables[-1].append(l)

def get_number_of_rows(table):
    return next((i + 1 for i in range(len(table) - 1) if all(i - j < 0 or i + j + 1 >= len(table) or table[i - j] == table[i + j + 1] for j in range(len(table)))), None)

print(sum(get_number_of_rows(list(zip(*table))) or 100 * get_number_of_rows(table) for table in tables))