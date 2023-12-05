#!/usr/bin/env python3

from sys import stdin

inp = stdin.read().split('\n\n')
seeds = [int(s) for s in inp[0].split()[1:]]
range_groups = [[[int(n) for n in r.split()] for r in g.split('\n')[1:]] for g in inp[1:]]

def get_location(n):
    for rg in range_groups:
        for r in rg:
            if r and r[1] <= n < r[1] + r[2]:
                n += r[0] - r[1]
                break
    return n

print(min(map(get_location, seeds)))
