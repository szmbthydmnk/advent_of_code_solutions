#!/usr/bin/python3
import sys
from functools import cache
from collections import defaultdict, Counter, deque
import z3
import Functions as F


def read(file_path):
    with open(file_path, 'r') as file:
        return file.read()

D = read("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Device_connections_File.txt")
E = {}
for line in D.splitlines():
    x, ys = line.split(':')
    ys = ys.split()
    E[x] = ys

print(E)
@cache
def part1(x):
    if x=='out':
        return 1
    else:
        return sum(part1(y) for y in E[x])

@cache
def part2(x, seen_dac, seen_fft):
    if x=='out':
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for y in E[x]:
            new_seen_dac = seen_dac or y=='dac'
            new_seen_fft = seen_fft or y=='fft'
            ans += part2(y, new_seen_dac, new_seen_fft)
        return ans

print(part1('you'))
print(part2('svr', False, False))