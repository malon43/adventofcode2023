#!/usr/bin/env python3

from sys import stdin
from itertools import islice
from functools import reduce

def in_pairs(iterable):  # python 3.12 wen?
    it = iter(iterable)
    while batch := tuple(islice(it, 2)):
        yield batch


def get_offset_ranges(ranges, source_ranges_offsets):
    i = j = 0
    in_sr = in_r = False
    res = []
    pos = -1
    while i < len(ranges) and j < len(source_ranges_offsets):
        rng = ranges[i]
        *src_rng, offset = source_ranges_offsets[j]
        offset *= in_sr

        if in_r:
            if pos < src_rng[in_sr] <= rng[1]:
                res.append((pos + offset, src_rng[in_sr] + offset))
                pos = src_rng[in_sr]
            elif pos < rng[1] < src_rng[in_sr]:
                res.append((pos + offset, rng[1] + offset))
        elif rng[0] < src_rng[in_sr]:
            pos = rng[0]

        if rng[in_r] < src_rng[in_sr]:
            i += in_r
            in_r = not in_r
        else:
            j += in_sr
            in_sr = not in_sr

    if i < len(ranges):
        res.append((max(ranges[i][0], pos), ranges[i][1]))
        res.extend(ranges[i + 1:])

    return sorted(res) # runs just fine without unionizing ranges, on larger inputs it might be worth considering


inp = stdin.read().split('\n\n')

print(min(s[0] for s in reduce(get_offset_ranges, (sorted((s, s + c, d - s) for d, s, c in(map(int, r.split()) for r in islice(g.split('\n'), 1, None) if r.strip())) for g in islice(inp, 1, None)), sorted([(int(t[0]), int(t[0]) + int(t[1])) for t in in_pairs(islice(inp[0].split(), 1, None))]))))
