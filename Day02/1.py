#!/usr/bin/env python3

from sys import stdin
from collections import Counter


class Choice:
    def __init__(self, colors):
        self.colors = colors

    def possible(self, colors_max):
        return self.colors <= colors_max

    @classmethod
    def parse(cls, choice):
        colors = Counter()
        for count, color in map(str.split, choice.split(', ')):
            colors[color] += int(count)
        return cls(colors)


class Game:
    def __init__(self, id_, choices):
        self.id = id_
        self.choices = choices

    def possible(self, colors_max):
        return all(c.possible(colors_max) for c in self.choices)

    @classmethod
    def parse(cls, line):
        prefix, ch = line.split(': ')
        id_ = int(prefix.split()[1])
        choices = list(map(Choice.parse, ch.split('; ')))
        return cls(id_, choices)


COLORS_MAX = Counter({'red': 12, 'green': 13, 'blue': 14})
print(sum(g.id for g in map(Game.parse, map(str.strip, stdin)) if g.possible(COLORS_MAX)))
