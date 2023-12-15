#!/usr/bin/env python3

from sys import stdin
from functools import reduce

print(sum(reduce(lambda last, x: (last + ord(x)) * 17 % 256, sequence, 0) for sequence in stdin.read().replace('\n', '').split(',')))


