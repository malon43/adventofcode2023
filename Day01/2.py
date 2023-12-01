#!/usr/bin/env python3

from sys import stdin
from re import search

digits = {n: str(i + 1) for i, n in enumerate(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))}

print(sum(int(digits.get(a, a) + digits.get(b, b)) for a, b in ((search('[0-9]|' + '|'.join(digits), line)[0], search('[0-9]|' + '|'.join(map(lambda x: x[::-1], digits)), line[::-1])[0][::-1]) for line in stdin)))
