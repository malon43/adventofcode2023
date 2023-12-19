#!/usr/bin/env python3

from sys import stdin
from re import match
from itertools import takewhile
from functools import reduce


def get_operation(category, operation, rating, target):
    rating = int(rating)
    def op(part):
        not_part = part.copy()
        part = part.copy()

        start, end = part[category]
        if operation == '>':
            not_part[category], part[category] = (start, min(rating, end)), (max(rating + 1, start), end)
        else:
            part[category], not_part[category] = (start, min(rating - 1, end)), (max(rating, start), end)
        return target, part if part[category][0] <= part[category][1] else None, not_part if not_part[category][0] <= not_part[category][1] else None

    return op


def get_otherwise(target):
    return lambda part: (target, part, None)


def get_possible_parts(workflows, not_part, workflow='in'):
    if workflow == 'A':
        return [not_part]

    res = []
    for operation in workflows[workflow]:
        target, part, not_part = operation(not_part)

        if part is not None:
            res.extend(get_possible_parts(workflows, part, target))

        if not_part is None:
            break

    return res


workflows = {'R': [(lambda _: (None, None, None))]}
for workflow_name, workflow in map(lambda line: match(r'([a-z]+){(.+)}', line).groups(), takewhile(bool, map(str.strip, stdin))):
    for step in workflow.split(','):
        workflows.setdefault(workflow_name, []).append(get_operation(*match(r'([xmas])([<>])([0-9]+):(R|A|[a-z]+)', step).groups()) if ':' in step else get_otherwise(step))

print(sum(reduce(lambda a, pv: a * (pv[1] - pv[0] + 1), part.values(), 1) for part in get_possible_parts(workflows, {c: (1, 4000) for c in 'xmas'})))