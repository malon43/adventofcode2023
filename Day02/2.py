#!/usr/bin/env python3

from sys import stdin
from collections import Counter
from functools import reduce
from operator import mul, or_


class Choice:
    def __init__(self, colors):
        self.colors = colors

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

    def get_max_color(self):
        return reduce(or_, (c.colors for c in self.choices))

    def get_power(self):
        return reduce(mul, self.get_max_color().values())

    @classmethod
    def parse(cls, line):
        prefix, ch = line.split(':')
        id_ = int(prefix.split()[1])
        choices = list(map(Choice.parse, ch.split('; ')))
        return cls(id_, choices)


print(sum(map(Game.get_power, map(Game.parse, map(str.strip, stdin)))))
