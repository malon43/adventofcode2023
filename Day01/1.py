#!/usr/bin/env python3

from sys import stdin
from re import findall
from functools import partial

print(sum(int(x[0] + x[-1]) for x in map(partial(findall, '[0-9]'), stdin)))
