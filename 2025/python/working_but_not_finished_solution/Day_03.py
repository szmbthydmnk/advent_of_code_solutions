# Advent of Code - 2025
# Day 3: Encrypted Message Decoder

import Functions as F
import numpy as np

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Battery_Banks_File.txt")

def GetLineValue(line : str) -> list[int]:
    line = line.strip()
    values = [int(char) for char in line]
    return values

def max_with_indices(lst):
    if not lst:
        return None, []  # handle empty list

    max_val = max(lst)
    indices = [i for i, x in enumerate(lst) if x == max_val]
    return max_val, indices


# Search fo the larges joltage number in each bank from the 1st to the end - 1st element.
# Choose the fisrt occurance at index "k" and search for the next largest element in the remaining bank from index "k" to end.
# Put together these two integers to form the final joltage number.


Battery_Banks = [GetLineValue(line) for line in File]

# Part 1: Find the total joltage sum
Joltage_sum = 0

for i in range(len(Battery_Banks)):
    Bank = Battery_Banks[i]

    max_joltage, indices = max_with_indices(Bank[:-1])  # Exclude the last element
   
    k = indices[0]
    next_max_joltage, _ = max_with_indices(Bank[(k + 1):])  # Search from index k to the end, excluding last element
        
    Joltage_sum += (max_joltage * 10 + next_max_joltage)


#def FindMaxJoltage(Bank: list[int]) - int;
print(f"Total joltage sum:\t {Joltage_sum}")
print(["-"*100])

# Part 2: Find the 12 digit Joltage sums

# It's like a nonogram!
# Saerch for max digit from start to end - 11
# Take the first, mark the index, search for max in the remaining part of the list from that index to end - 10
# Repeat until 12 digits are found

Joltage_sum_2 = 0

for i in range(len(Battery_Banks)):
    Bank = Battery_Banks[i]

    Joltage_digits = []
    latest_max_joltage_index = -1
    for no_of_digit in range(12):
        # Only "tricky" part: take care of pyhton indexing
        end_index = len(Bank) if no_of_digit == 11 else (-11 + no_of_digit)

        max_joltage, indices = max_with_indices(Bank[latest_max_joltage_index + 1:end_index])
        Joltage_digits.append(max_joltage)
        latest_max_joltage_index += indices[0] + 1

    Joltage_sum_2 += int(''.join(map(str, Joltage_digits)))
    
print(f"Total 12-digit joltage sum:\t {Joltage_sum_2}")