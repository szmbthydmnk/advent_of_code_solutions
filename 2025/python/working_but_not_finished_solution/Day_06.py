# Advent of Coda - 2025
# Dominik Szombathy
# 2025.12.06

# Day 6 - Trash compactor

import Functions as F
import itertools
import math
import re

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Math_Homework_File.txt")

def split_columns(lines):
    if isinstance(lines, str):
        lines = lines.splitlines()
    else:
        lines = [ln.rstrip("\n") for ln in lines]

    if not lines:
        return []

    # Keep alignment: pad lines to same length
    maxlen = max(len(ln) for ln in lines)
    lines = [ln.ljust(maxlen) for ln in lines]

    # Find column spans: positions where any line has a non-space char
    any_non_space = [any(ln[c] != " " for ln in lines) for c in range(maxlen)]
    spans = []
    c = 0
    while c < maxlen:
        if any_non_space[c]:
            start = c
            while c < maxlen and any_non_space[c]:
                c += 1
            spans.append((start, c))  # slice indices [start:c)
        else:
            c += 1

    # For each span, check that the last line segment contains '+' or '*',
    # then collect non-empty trimmed entries from all previous lines
    result = []
    last_line = lines[-1]
    for start, end in spans:
        seg = last_line[start:end]
        ending_char = next((ch for ch in seg if ch in "+*"), None)
        if ending_char:
            column = []
            for row in lines[:-1]:
                val = row[start:end].strip()
                if val:
                    column.append(val)
            if column:
                result.append((column, ending_char))

    return result

Math_Problem_Numbees = split_columns(File)
Math_Problem_Numbees = [(list(map(int, col)), op) for col, op in Math_Problem_Numbees]

maths_sum = 0
for math_problem_index in range(len(Math_Problem_Numbees)):
    if Math_Problem_Numbees[math_problem_index][1] == "+":
        maths_sum += sum(Math_Problem_Numbees[math_problem_index][0])
    elif Math_Problem_Numbees[math_problem_index][1] == "*":
        maths_sum += math.prod(Math_Problem_Numbees[math_problem_index][0])

print(maths_sum)

def split_columns_to_matrix(lines):
    if isinstance(lines, str):
        lines = lines.splitlines()
    else:
        lines = [ln.rstrip("\n") for ln in lines]

    if not lines:
        return []

    # Pad lines to same length to preserve alignment
    maxlen = max(len(ln) for ln in lines)
    lines = [ln.ljust(maxlen) for ln in lines]

    # Find contiguous spans of columns that contain any non-space in any row
    any_non_space = [any(ln[c] != " " for ln in lines) for c in range(maxlen)]
    spans = []
    c = 0
    while c < maxlen:
        if any_non_space[c]:
            start = c
            while c < maxlen and any_non_space[c]:
                c += 1
            spans.append((start, c))
        else:
            c += 1

    # Build a matrix (rows x width) for each span, excluding the last line
    matrices = []
    for start, end in spans:
        matrix = [list(row[start:end]) for row in lines[:-1]]
        matrices.append(matrix)

    return matrices


Matrices = split_columns_to_matrix(File)
print((Matrices[2]))

def MatrixColumnsToNumber(Matrix):
    Numbers = []
    if not Matrix or not any(Matrix):
        return Numbers

    rows = len(Matrix)
    cols = max(len(r) for r in Matrix)

    for c in range(cols):
        # build the column string top-to-bottom, treating missing cells as spaces
        s = ''.join((Matrix[r][c] if c < len(Matrix[r]) else ' ') for r in range(rows)).strip()
        if not s:
            continue
        # find first integer in the column string (handles signs)
        m = re.search(r'-?\d+', s)
        if m:
            Numbers.append(int(m.group()))
        else:
            # fallback: try direct int conversion of the trimmed string
            try:
                Numbers.append(int(s))
            except Exception:
                # ignore non-parsable columns
                pass

    return Numbers


print(MatrixColumnsToNumber(Matrices[2]))
print(len(Matrices))
Maths_sum_2 = 0
for i in range(len(Matrices)):
    N = MatrixColumnsToNumber(Matrices[i])
    print(N)
    if Math_Problem_Numbees[i][1] == "+":
        print(sum(N))
        Maths_sum_2 += sum(N)
    else:
        print(math.prod(N))
        Maths_sum_2 += math.prod(N)

print(Maths_sum_2)