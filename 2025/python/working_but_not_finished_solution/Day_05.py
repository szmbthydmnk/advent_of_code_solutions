# Advent of Code - 2025
# Day 5 - Cafeteria

import Functions as F

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Inventory_management_File.txt")

Ranges_File = File[:185]
ID_File = File[186:]

Ranges = F.SeparateRanges(Ranges_File)

Ranges.sort(key=lambda x: x[0])  # Sort ranges by their start value
Merged_Ranges = []
for current in Ranges:
    if not Merged_Ranges or Merged_Ranges[-1][1] < current[0]:
        Merged_Ranges.append(current)
    else:
        Merged_Ranges[-1][1] = max(Merged_Ranges[-1][1], current[1])

# print(len(Ranges))
# print(len(Merged_Ranges))
# hopp, only half of stuff to check

# Part 1:

fresh_items = 0

for id_index in range(len(ID_File)):
    for start, end in Merged_Ranges:
        if start <= int(ID_File[id_index]) <= end:
            fresh_items += 1
            break

print(fresh_items)

# Part 2:
Possible_Fresh_IDs = 0
for start, end in Merged_Ranges:
    Possible_Fresh_IDs += end - start + 1

print(Possible_Fresh_IDs)