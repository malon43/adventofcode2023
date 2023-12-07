#!/usr/bin/env python3

from sys import stdin
from collections import Counter

CARDS = {c: i for i, c in enumerate("23456789TJQKA")}

HAND_RANKS = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5],
]


def get_hand_score(hand):
    score = HAND_RANKS.index(sorted(Counter(hand).values())) * len(CARDS) ** len(hand)
    score += sum(CARDS[c] * len(CARDS) ** i for i, c in enumerate(reversed(hand)))
    return score


print(sum(bid * (i + 1) for i, (_, bid) in enumerate(sorted(((get_hand_score(hand), int(bid)) for hand, bid in map(str.split, stdin))))))

