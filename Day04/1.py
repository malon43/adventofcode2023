#!/usr/bin/env python3

from sys import stdin

print(sum((lambda matching_count: 2 ** (matching_count - 1) if matching_count else 0)(len(set(card.split()) & set(mine.split()))) for card, mine in map(lambda x: x.strip().split(': ')[1].split(' | '), stdin)))