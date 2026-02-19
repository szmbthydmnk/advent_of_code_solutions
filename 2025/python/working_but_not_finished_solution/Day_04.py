# Advent of code - 2025
# Day 4: Helping the elves move the papaer rolls

import Functions as F
import numpy as np
import time

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Paper_Roll_Map_File.txt")

def FileToMap(File: list[str]) -> list[list[str]]:
    """Convert file lines into a 2D map representation."""
    Map = []
    for line in File:
        line = line.strip()
        Map.append([char for char in line])
    return Map

Paper_Roll_Map = FileToMap(File)

def IsThisPaperRollMovable(Map: list[list[str]], row: int, col: int, dimensions : list[int]) -> bool:

    if Map[row][col] == '.':
        Warning("My man, this ain't no paper roll, get a grip!")
        return False
    
    roll_height, roll_width = dimensions

    # Check whether there are less than 4 occupied spaces around the roll
    filled_count = 0 

    # Generate list with neighboring coordinates, don't add places that are outside, no BC
    neighbors = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (0 <= r < len(Map)) and (0 <= c < len(Map[0])) and not (r == row and c == col):
                neighbors.append((r, c))
    
    # Now check the neighboring cells:
    for r, c in neighbors:
        if Map[r][c] != '.':
            filled_count += 1
    
    if filled_count >= 4:
        return False
    
    return True


def NeighborCounter(Map: list[list[str]], row: int, col: int, dimensions : list[int]) -> int:

    if Map[row][col] == '.':
        Warning("My man, this ain't no paper roll, get a grip!")
        return False
    
    roll_height, roll_width = dimensions

    # Check whether there are less than 4 occupied spaces around the roll
    filled_count = 0 

    # Generate list with neighboring coordinates, don't add places that are outside, no BC
    neighbors = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (0 <= r < len(Map)) and (0 <= c < len(Map[0])) and not (r == row and c == col):
                neighbors.append((r, c))
    
    # Now check the neighboring cells:
    for r, c in neighbors:
        if Map[r][c] != '.':
            filled_count += 1
    
    return filled_count


def Warning(message: str):
    print(f"Warning: {message}")

#print(f"Matrix dimensions: {len(Paper_Roll_Map)} rows x {len(Paper_Roll_Map[0])} columns")
#print(IsThisPaperRollMovable(Paper_Roll_Map, 6, 2, [135, 135]))
start_t = time.perf_counter()
Number_of_movables = 0
for row in range(len(Paper_Roll_Map)):
    for col in range(len(Paper_Roll_Map[0])):
        if Paper_Roll_Map[row][col] == '.':
            continue
        if IsThisPaperRollMovable(Paper_Roll_Map, row, col, [135, 135]):
            Number_of_movables += 1

end_t = time.perf_counter()
print("Elapsed:", end_t - start_t, "[sec]")

print(f"Part 1:\nNumber of movable paper rolls:\t\t {Number_of_movables}")      
print(["-"*100])

# Part - 2:

# So we want to remove the movable papers on the go, but still we might want to revisit the places we've been to.
# A while loop could do this job, but a recursive function might be more in line with the spirit of AOC.

# Let's do the  brute fore version first to get the logic right:

# create a working copy of the map to modify without altering the original
temp_map = [row[:] for row in Paper_Roll_Map]

start_t = time.perf_counter()

All_removed_rolls = 0
Number_of_removed_rolls = -1
k = 0
while Number_of_removed_rolls != 0:
    k += 1
    Number_of_removed_rolls = 0
    for row in range(len(temp_map)):
        for col in range(len(temp_map[0])):
            if temp_map[row][col] == '.':
                continue
            if IsThisPaperRollMovable(temp_map, row, col, [135, 135]):
                Number_of_removed_rolls += 1
                temp_map[row][col] = '.'

    All_removed_rolls += Number_of_removed_rolls

end_t = time.perf_counter()
print("Elapsed:", end_t - start_t, "[sec]")

print("Part 2:\nAll possible removed rolls:\t", All_removed_rolls,"\t In ", k, " rounds. ")

print(["-"*100])

# a more sophisticated approach:
# Map out the number of neighbors
# Start from a corner and start to remove the rolls, for each removed roll, visit it's neighbors and adjust the neighbor counter
N = 135
temp_map = Paper_Roll_Map




start_t = time.perf_counter()

Neighbor_map = [[0 for _ in range(135)] for _ in range(135)]

for r in range(135):
    for c in range(135):
        if temp_map[r][c] == ".":
            Neighbor_map[r][c] = -1
        else:
            Neighbor_map[r][c] = NeighborCounter(temp_map, r, c, [135, 135])



queue = []
for r in range(135):
    for c in range(135):        
        if 0 <= Neighbor_map[r][c] < 4:
            queue.append([r, c])

while queue:
    r, c = queue.pop(0)
    if 0 <= Neighbor_map[r][c] < 4:
        Neighbor_map[r][c] = -2

        for nr in range(r - 1, r + 2):
            for nc in range(c - 1, c + 2):
                if (0 <= nr < N) and (0 <= nc < N) and not (nr == r and nc == c):
                    if Neighbor_map[nr][nc] > 0:
                        Neighbor_map[nr][nc] -= 1
                        if 0 <= Neighbor_map[nr][nc] < 4:
                            queue.append((nr, nc))

end_t = time.perf_counter()
print("Elapsed:", end_t - start_t, "[sec]")
num_minus_two = sum(1 for row in Neighbor_map for val in row if val == -2)
print("Number of -2 entries in Neighbor_map:", num_minus_two)
