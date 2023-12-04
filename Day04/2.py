#!/usr/bin/env python3

from sys import stdin

cards = [len(set(card.split()) & set(mine.split())) for card, mine in map(lambda x: x.strip().split(': ')[1].split(' | '), stdin)][::-1]

for i, m in enumerate(cards):
    cards[i] = sum(cards[i - m:i]) + 1

print(sum(cards))