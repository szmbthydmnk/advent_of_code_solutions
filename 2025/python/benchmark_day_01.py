#!/usr/bin/env python3
from timeit import timeit
from pathlib import Path
from typing import Iterator, Tuple
from Functions_2025 import read_lines

INPUT_PATH = Path("Advent_of_Code_2025/input_files") / "Password_File.txt"

def get_rotation_params(line: str) -> Tuple[str, int]:
    direction = line[0]
    rotation_value = int(line[1:].strip())
    return direction, rotation_value

# WRAPPER FUNCTIONS - timeit SAFE
def benchmark_part1():
    rotations = (get_rotation_params(line) for line in read_lines(INPUT_PATH))
    dial_position = 50
    count = 0
    for direction, rotation_value in rotations:
        rotation_angle = rotation_value if direction == 'R' else -rotation_value
        dial_position = (dial_position + rotation_angle) % 100
        if dial_position == 0:
            count += 1
    return count

def benchmark_part2():
    rotations = (get_rotation_params(line) for line in read_lines(INPUT_PATH))
    dial_position = 50
    count = 0
    for direction, rotation_value in rotations:
        rotation_angle = rotation_value if direction == 'R' else -rotation_value
        dial_position += rotation_angle
        if dial_position < 0:
            if dial_position % 100 == 0:
                count += abs(dial_position) // 100
            else:
                count += abs(dial_position) // 100 + 1
        elif dial_position >= 100:
            count += dial_position // 100
        dial_position %= 100
    return count

# BENCHMARKS - No external vars!
number_of_runs = 10000
print(f"=== PART 1 BENCHMARK ({number_of_runs} runs) ===")
t1 = timeit('benchmark_part1()', number=number_of_runs, globals=globals())
print(f"Avg: {t1/number_of_runs:.7f}ms")

print("\n=== PART 2 BENCHMARK (1,000 runs) ===")
t2 = timeit('benchmark_part2()', number=number_of_runs, globals=globals())
print(f"Avg: {t2/number_of_runs:.7f}ms")

print(f"\nP1/P2 ratio: {t1/t2:.2f}x")
