#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2025 - Day 01 - Secret Entrance
Official website: https://adventofcode.com/2025/day/1
Solution by Dominik Szombathy
Date: 2025-12-01
"""


from typing import Tuple, Iterator
from pathlib import Path
from Functions_2025 import read_lines

def get_rotation_params(line: str) -> Tuple[str, int]:
    """
    Parse a rotation line into direction ('L'/'R') and distance (int).
    
    :param line: Single line like "L68" or "R48" from input file.
    :type line: str
    :return: Tuple of (direction, distance)
    :rtype: Tuple[str, int]
    """
    direction = line[0]
    rotation_value = int(line[1:].strip())  # Safe: strip whitespace
    return direction, rotation_value

def part1(rotations: Iterator[Tuple[str, int]]) -> int:
    """
    Count times dial points at 0 *after* each rotation (starts at 50).
    
    :param rotations: Iterator of (direction, distance) tuples
    :type rotations: Iterator[Tuple[str, int]]
    :return: Password count (times at 0)
    :rtype: int

    Solution approach:
    - Go through rotations, update dial position, modulo 100, check for '0'.
    """
    dial_position = 50 # Starting position
    count = 0 # Password counter

    for direction, rotation_value in rotations:
        rotation_angle = rotation_value if direction ==  'R' else -rotation_value
        dial_position = (dial_position + rotation_angle) % 100
        if dial_position == 0:
            count += 1
    return count


def part2(rotations: Iterator[Tuple[str, int]]) -> int:
    """
    Count times dial crosses 0 during rotations (starts at 50).

    :param rotations: Iterator of (direction, distance) tuples
    :type rotations: Iterator[Tuple[str, int]]
    :return: Password count (times crossed 0)
    :rtype: int

    Solution approach:
    - Track dial position, count crossings of '0' during each rotation.
    """
    dial_position = 50 # Starting position
    count = 0 # Password counter

    for direction, rotation_value in rotations:
        rotation_angle = rotation_value if direction ==  'R' else -rotation_value
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
    
def main() -> None:
    # part 1
    input_path = Path("Advent_of_Code_2025/input_files/Password_File.txt")
    rotations = (get_rotation_params(line) for line in read_lines(input_path))

    print(f"Part 1 answer: The password to open the door is {part1(rotations)}")

    # part 2
    rotations = (get_rotation_params(line) for line in read_lines(input_path))

    print(f"Part 2 answer: The password to open the door is {part2(rotations)}")


if __name__ == "__main__":
    main()
