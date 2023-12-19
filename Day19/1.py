#!/usr/bin/env python3

from sys import stdin
from re import match
from itertools import takewhile
from operator import lt, gt

def get_operation(category, operation, rating, target):
    return lambda part: target if ((gt if operation == '>' else lt)(part[category], int(rating))) else None


def get_otherwise(target):
    return lambda _: target


def is_accepted(workflows, part, workflow='in'):
    while workflow not in ('R', 'A'):
        for operation in workflows[workflow]:
            if workflow := operation(part):
                break
    return workflow == 'A'


workflows = {}
for workflow_name, workflow in map(lambda line: match(r'([a-z]+){(.+)}', line).groups(), takewhile(bool, map(str.strip, stdin))):
    for step in workflow.split(','):
        workflows.setdefault(workflow_name, []).append(get_operation(*match(r'([xmas])([<>])([0-9]+):(R|A|[a-z]+)', step).groups()) if ':' in step else get_otherwise(step))
parts = [dict((a, int(b)) for a,b in(val.split('=') for val in line.strip('{}\n').split(','))) for line in stdin]

print(sum(sum(part.values()) for part in parts if is_accepted(workflows, part)))