# Advent of Code 2025
# Szombathy Dominik
# 2025.12.19

# Day 9 - Movie Theater

import Functions as F
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/red_tiles_File.txt")

print(File[0])

def coordinates_from_line(line):
    Coordinate_str = line.split(",")
    Coordinates = []
    for item in Coordinate_str:
        Coordinates.append(int(item))
    return Coordinates

print(coordinates_from_line(File[0])[1])

def calculate_rectangle_area(coord_1, coord_2):

    x = abs(coord_1[0] - coord_2[0]) + 1
    y = abs(coord_1[1] - coord_2[1]) + 1

    return x * y

print(coordinates_from_line(File[0]))
print(coordinates_from_line(File[1]))
print(calculate_rectangle_area(coordinates_from_line(File[0]), coordinates_from_line(File[1])))

Coordinates = []
for line in File:
    Coordinates.append(coordinates_from_line(line))

Areas = []
for i in range(len(Coordinates)):
    for j in range(i + 1, len(Coordinates)):
        Areas.append(calculate_rectangle_area(Coordinates[i], Coordinates[j]))

print(max(Areas))

# Part 2

# First let's see the map:
x_coords = [x[0] for x in Coordinates]
y_coords = [y[1] for y in Coordinates]
N = len(Coordinates)
# "compress coordinates"

xs = set()
ys = set()

for x, y in Coordinates:
    for dx in (-1, 0, 1):
        xs.add(x + dx)
    for dy in (-1, 0, 1):
        ys.add(y + dy)

xs = sorted(xs)
ys = sorted(ys)

x_id = {x: i for i, x in enumerate(xs)}
y_id = {y: i for i, y in enumerate(ys)}

W = len(xs)
H = len(ys)

grid = np.zeros((H, W), dtype=np.int8)

def draw_edge(p1, p2):
    x1, y1 = x_id[p1[0]], y_id[p1[1]]
    x2, y2 = x_id[p2[0]], y_id[p2[1]]

    if x1 == x2:
        a, b = sorted([y1, y2])
        grid[a:b+1, x1] = 1
    else:
        a, b = sorted([x1, x2])
        grid[y1, a:b+1] = 1

for i in range(N):
    draw_edge(Coordinates[i], Coordinates[(i+1) % N])

# -----------------------------
# Flood fill exterior
# -----------------------------

outside = np.zeros_like(grid)
q = deque()

for x in range(W):
    q.append((0, x))
    q.append((H-1, x))
for y in range(H):
    q.append((y, 0))
    q.append((y, W-1))

while q:
    y, x = q.popleft()
    if not (0 <= x < W and 0 <= y < H):
        continue
    if outside[y, x] or grid[y, x] == 1:
        continue
    outside[y, x] = 1
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        q.append((y+dy, x+dx))

# allowed = boundary + interior
allowed = (grid == 1) | (outside == 0)

# -----------------------------
# Prefix sum of forbidden tiles
# -----------------------------

bad = (~allowed).astype(np.int8)
ps = bad.cumsum(axis=0).cumsum(axis=1)

def forbidden_in_rect(x1, y1, x2, y2):
    res = ps[y2, x2]
    if x1 > 0: res -= ps[y2, x1-1]
    if y1 > 0: res -= ps[y1-1, x2]
    if x1 > 0 and y1 > 0: res += ps[y1-1, x1-1]
    return res

# -----------------------------
# Enumerate red corner rectangles
# -----------------------------

best = 0

for i in range(N):
    x1, y1 = Coordinates[i]
    for j in range(i+1, N):
        x2, y2 = Coordinates[j]

        cx1, cx2 = sorted([x_id[x1], x_id[x2]])
        cy1, cy2 = sorted([y_id[y1], y_id[y2]])

        if forbidden_in_rect(cx1, cy1, cx2, cy2) == 0:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            best = max(best, area)

print(best)