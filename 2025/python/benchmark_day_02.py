#!/usr/bin/env python3
from timeit import timeit
from typing import Callable
from pathlib import Path
from Functions_2025 import read_lines

def separate_ranges(lines: list[str]) -> list[list[int]]:
    """
    Seprates the ranges of the input files into [start, finish] pairs
    
    :param File: Input file lines
    :type File: list[str]
    :return: List of ranges
    :rtype: list[list[int]]
    """
    ranges: list[list[int]] = []             # List to hold the ranges
    for line in lines:       # There is probably only one line in this file 
        line = line.strip() 
        range_pairs = line.split(',')   # Split by comma to get individual ranges
        for pair in range_pairs:        # Split each range into start and end
            start, end = pair.split('-')    
            ranges.append([int(start), int(end)])
    return ranges

# Flight check 1:
def simplify_ranges(ranges: list[list[int]]) -> list[list[int]]:
    """
    Merge overlapping or adjacent ranges.

    Example:
        [[1, 8], [7, 9]] -> [[1, 9]]

    :param ranges: Raw ranges from the input file.
    :type ranges: list[list[int]]
    :return: Simplified/merged ranges.
    :rtype: list[list[int]]
    """
    if not ranges:
        return []

    ranges.sort(key=lambda r: r[0])

    merged: list[list[int]] = []
    for current in ranges:
        if not merged or merged[-1][1] < current[0] - 0:
            # No overlap
            merged.append(current)
        else:
            # Overlapping; extend the end
            merged[-1][1] = max(merged[-1][1], current[1])

    return merged

#Flight check 2:
def report_large_ranges(ranges: list[list[int]], threshold: int = 1_000_000) -> None:
    """
    Simple sanity check: print a warning for very large ranges.

    :param ranges: List of [start, end] ranges.
    :type ranges: list[list[int]]
    :param threshold: Size above which a range is reported.
    :type threshold: int
    """
    for start, end in ranges:
        size = end - start + 1
        if size >= threshold:
            print(f"Large range detected: {start}-{end} (size: {size})")

# Helper 1:
def is_ID_repeated_twice(ID: int) -> bool:
    """
    Check whether an ID consists of some sequence of digits repeated exactly twice.

    Examples:
        55      -> '5' repeated twice      -> invalid (True)
        6464    -> '64' repeated twice     -> invalid (True)
        123123  -> '123' repeated twice    -> invalid (True)
        101     -> not two equal halves    -> valid  (False)

    None of the IDs have leading zeroes in the input, but we explicitly
    reject those as non-IDs.

    :param ID: The ID to check.
    :type ID: int
    :return: True if the ID is invalid (repeated twice), False otherwise.
    :rtype: bool
    """
    s = str(ID)

    # Explicitly reject leading zero IDs
    if s[0] == "0":
        return False

    n = len(s)

    # Must be exactly two equal halves -> even length
    if n % 2 != 0:
        return False

    half = n // 2
    return s[:half] == s[half:]

# Helper 2:
def is_ID_repeated_Nth(ID: int) -> bool:
    """
    Check whether an ID consists of some sequence repeated N >= 2 times.

    This is a generalized version where the entire string is constructed as
    seq * k for some k >= 2.

    :param ID: The ID to check.
    :type ID: int
    :return: True if the ID is invalid (repeated pattern), False otherwise.
    :rtype: bool
    """
    s = str(ID)

    if s[0] == "0":
        return False

    n = len(s)
    # Try all possible pattern lengths
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len != 0:
            continue
        repeats = n // pattern_len
        if repeats < 2:
            continue
        pattern = s[:pattern_len]
        if pattern * repeats == s:
            return True

    return False

def part12(ranges: list[list[int]], validation_func: Callable[[int], bool]) -> int:
    """
    Sum all IDs within the given ranges for which 'invalid_predicate' returns True.

    :param ranges: List of [start, end] integer ranges.
    :type ranges: list[list[int]]
    :param invalid_predicate: Function returning True for invalid IDs.
    :type invalid_predicate: Callable[[int], bool]
    :return: Sum of all invalid IDs found in the ranges.
    :rtype: int
    """
    total = 0
    for start, end in ranges:
        for ID in range(start, end + 1):
            if validation_func(ID):
                total += ID
    return total

# -----------------------------------
# Benchmarking
# -----------------------------------
input_path = Path("Advent_of_Code_2025/input_files/ID_Ranges_File.txt")
lines = read_lines(input_path)
Ranges = separate_ranges(lines) 
Merged_Ranges = simplify_ranges(Ranges)

report_large_ranges(Merged_Ranges)




number_of_runs = 2
print(f"=== PART 1 BENCHMARK ({number_of_runs} runs) ===")
t1 = timeit('part12(Merged_Ranges, is_ID_repeated_twice)', number = number_of_runs, globals=globals())
print(f"Avg: {t1/number_of_runs:.7f}")

print(f"=== PART 2 BENCHMARK ({number_of_runs} runs) ===")
t2 = timeit('part12(Merged_Ranges, is_ID_repeated_Nth)', number = number_of_runs, globals=globals())
print(f"Avg: {t2/number_of_runs:.7f}")
