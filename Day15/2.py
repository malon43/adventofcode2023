#!/usr/bin/env python3

from sys import stdin
from functools import reduce
from re import match


def find_lens(box, label):
    for i, (ll, _) in enumerate(box):
        if ll == label:
            return i
    return None


boxes = [[] for _ in range(256)]

for label, operation, number in (match('([a-z]+)([-=])([0-9]*)', sequence).groups() for sequence in stdin.read().replace('\n', '').split(',')):
    box_n = reduce(lambda last, x: (last + ord(x)) * 17 % 256, label, 0)
    i = find_lens(boxes[box_n], label)
    if operation == '-' and i is not None:
        boxes[box_n].pop(i)
    elif operation == '=':
        if i is None:
            boxes[box_n].append((label, int(number)))
        else:
            boxes[box_n][i] = (label, int(number))

print(sum(n * m * lfl for n, box in enumerate(boxes, 1) for m, (_, lfl) in enumerate(box, 1)))
